# Model Evaluation
from sklearn.metrics import classification_report
import pprint, json
import numpy as np

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)
            
def fpr_fnr(result_dict):
    FPR = (result_dict['per_class'][1]['all_positive'] - result_dict['per_class'][1]['true_positive'])/result_dict['per_class'][0]['all_true'] 
    FNR = (result_dict['per_class'][0]['all_positive'] - result_dict['per_class'][0]['true_positive'])/result_dict['per_class'][1]['all_true']
    print(f"FPR = {FPR}")
    print(f"FNR = {FNR}")
    result_dict['FPR'], result_dict['FNR'] = FPR, FNR
    return FPR, FNR, result_dict
    
def evaluate(model, X, y, class_names, batch_size):
    prediction_test_onehot = model.predict(X, batch_size=batch_size)
    prediction_test = prediction_test_onehot.argmax(axis=1).squeeze()
    return my_report(y, prediction_test, class_names)
    
def my_report(y_true, y_predict, class_names):
    results = {'per_class':dict(), 'total':dict()}
    y_true, y_predict = np.array(y_true), np.array(y_predict)
    for idx, cname in enumerate(class_names):
        TP = np.sum(np.logical_and((y_true == y_predict), (y_true == idx)))
        class_precision = TP / np.sum(y_predict == idx)
        class_recall = TP / np.sum(y_true == idx)
        class_f1 = 2*class_precision*class_recall / (class_precision + class_recall)
        results['per_class'][idx] = {'class_name': cname, 
                                     'true_positive': TP, 
                                     'all_positive': np.sum(y_predict == idx), 
                                     'all_true': np.sum(y_true == idx), 
                                     'class_precision': class_precision, 
                                     'class_recall': class_recall, 
                                     'class_f1': class_f1}
    
    results['total']['macro_precision'] = np.mean([results['per_class'][idx]['class_precision'] for idx in results['per_class']])
    results['total']['macro_recall'] = np.mean([results['per_class'][idx]['class_recall'] for idx in results['per_class']])
    results['total']['macro_f1'] = 2 * results['total']['macro_precision'] * results['total']['macro_recall'] / (results['total']['macro_precision'] + results['total']['macro_recall'])
    results['total']['accuracy'] = sum([results['per_class'][idx]['true_positive'] for idx in results['per_class']]) / len(y_true)
    results['total']['micro_precision'] = np.sum([results['per_class'][idx]['true_positive'] for idx in results['per_class']]) / np.sum([results['per_class'][idx]['all_positive'] for idx in results['per_class']])
    results['total']['micro_recall'] = np.sum([results['per_class'][idx]['true_positive'] for idx in results['per_class']]) / np.sum([results['per_class'][idx]['all_true'] for idx in results['per_class']])
    results['total']['micro_f1'] = 2 * results['total']['micro_precision'] * results['total']['micro_recall'] / (results['total']['micro_precision'] + results['total']['micro_recall'])
    pprint.pprint(results)
    return results
    
def evaluate_all_gender(model, class_names, batch_size, X_test_1, y_test_1, gender_test_1, X_test_2 = None, y_test_2 = None, gender_test_2 = None, result_path = None, model_name = ''):
    final_results = dict()

    print('Evaluate with the original test set:')
    fpr, fnr, result_dict_1 = fpr_fnr(evaluate(model, X_test_1, y_test_1, class_names, batch_size))
    final_results['Original'] = dict()
    final_results['Original']['all'] = result_dict_1

    print('\nFemale prediction:')
    y_female = [y_test_1[i] for i in range(len(y_test_1)) if gender_test_1[i] == 'F']
    X_female = np.array([X_test_1[i] for i in range(len(X_test_1)) if gender_test_1[i] == 'F'])
    fprf, fnrf, result_dict_1f = fpr_fnr(evaluate(model, X_female, y_female, class_names, batch_size))
    final_results['Original']['female'] = result_dict_1f

    print('\nMale prediction:')
    y_male = [y_test_1[i] for i in range(len(y_test_1)) if gender_test_1[i] == 'M']
    X_male = np.array([X_test_1[i] for i in range(len(X_test_1)) if gender_test_1[i] == 'M'])
    fprm, fnrm, result_dict_1m = fpr_fnr(evaluate(model, X_male, y_male, class_names, batch_size))
    final_results['Original']['male'] = result_dict_1m

    print('----------------------------------------------------')
    print(f'FPED = {np.abs(fpr-fprf) + np.abs(fpr-fprm)}')
    print(f'FNED = {np.abs(fnr-fnrf) + np.abs(fnr-fnrm)}')
    final_results['Original']['FPED'] = np.abs(fpr-fprf) + np.abs(fpr-fprm)
    final_results['Original']['FNED'] = np.abs(fnr-fnrf) + np.abs(fnr-fnrm)

    if X_test_2 is not None:
        print('Evaluate with the out-of-domain test set:')
        fpr, fnr, result_dict_2 = fpr_fnr(evaluate(model, X_test_2, y_test_2, class_names, batch_size))
        final_results['Out-of-domain-1'] = dict()
        final_results['Out-of-domain-1']['all'] = result_dict_2 

        print('\nFemale prediction:')
        y_female = [y_test_2[i] for i in range(len(y_test_2)) if gender_test_2[i] == 'F']
        X_female = np.array([X_test_2[i] for i in range(len(X_test_2)) if gender_test_2[i] == 'F'])
        fprf, fnrf, result_dict_2f = fpr_fnr(evaluate(model, X_female, y_female, class_names, batch_size))
        final_results['Out-of-domain-1']['female'] = result_dict_2f 

        print('\nMale prediction:')
        y_male = [y_test_2[i] for i in range(len(y_test_2)) if gender_test_2[i] == 'M']
        X_male = np.array([X_test_2[i] for i in range(len(X_test_2)) if gender_test_2[i] == 'M'])
        fprm, fnrm, result_dict_2m = fpr_fnr(evaluate(model, X_male, y_male, class_names, batch_size))
        final_results['Out-of-domain-1']['male'] = result_dict_2m 

        print('----------------------------------------------------')
        print(f'FPED = {np.abs(fpr-fprf) + np.abs(fpr-fprm)}')
        print(f'FNED = {np.abs(fnr-fnrf) + np.abs(fnr-fnrm)}')
        final_results['Out-of-domain-1']['FPED'] = np.abs(fpr-fprf) + np.abs(fpr-fprm)
        final_results['Out-of-domain-1']['FNED'] = np.abs(fnr-fnrf) + np.abs(fnr-fnrm)

    if result_path is not None:
        json.dump(final_results, open(result_path + f'results_{model_name}.json', 'w'), cls=NpEncoder)

def evaluate_all(model, class_names, batch_size, X_test_1, y_test_1, X_test_2 = None, y_test_2 = None, X_test_3 = None, y_test_3 = None, result_path = None, model_name = ''):
    final_results = dict()

    print('Evaluate with the original test set:')
    fpr_1, fnr_1, result_dict_1 = fpr_fnr(evaluate(model, X_test_1, y_test_1, class_names, batch_size))
    final_results['Original'] = result_dict_1

    if X_test_2 is not None:
        print('\nEvaluate with the out-of-domain test set 1:')
        fpr_2, fnr_2, result_dict_2 = fpr_fnr(evaluate(model, X_test_2, y_test_2, class_names, batch_size))
        final_results['Out-of-domain-1'] = result_dict_2
    
    if X_test_3 is not None:
        print('\nEvaluate with the out-of-domain test set 2:')
        fpr_3, fnr_3, result_dict_3 = fpr_fnr(evaluate(model, X_test_3, y_test_3, class_names, batch_size))
        final_results['Out-of-domain-2'] = result_dict_3

    if result_path is not None:
        json.dump(final_results, open(result_path + f'results_{model_name}.json', 'w'), cls=NpEncoder)

   
        
        