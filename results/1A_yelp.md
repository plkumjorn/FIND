<style>

.center-row td{
    text-align: center; 
    vertical-align: middle;    
}

tbody {
    display:block;
    width:13000px;
    overflow:auto;
}
thead, tbody tr {
    display:table;
    width:100%;
    table-layout:fixed;
}

td { white-space:pre }

</style>

# Experiment 1: Yelp

## Basic information
- **Task**: Sentiment analysis (of restaurant reviews)
- **Dataset**: Yelp
- **Classes**: Negative or Positive
- **Train/Dev/Test examples**: 500 / 100 / 38000
- **Problem**: The training data is very small.
- For more details, please see section 5 in the paper.

<hr>

## Word Clouds & Annotations

### Model 1: YelpSmall500_CNN_20200515014923
<table><tbody><tr class="center-row"><td><b>Feature 0</b></td><td><b>Feature 1</b></td><td><b>Feature 2</b></td><td><b>Feature 3</b></td><td><b>Feature 4</b></td><td><b>Feature 5</b></td><td><b>Feature 6</b></td><td><b>Feature 7</b></td><td><b>Feature 8</b></td><td><b>Feature 9</b></td><td><b>Feature 10</b></td><td><b>Feature 11</b></td><td><b>Feature 12</b></td><td><b>Feature 13</b></td><td><b>Feature 14</b></td><td><b>Feature 15</b></td><td><b>Feature 16</b></td><td><b>Feature 17</b></td><td><b>Feature 18</b></td><td><b>Feature 19</b></td><td><b>Feature 20</b></td><td><b>Feature 21</b></td><td><b>Feature 22</b></td><td><b>Feature 23</b></td><td><b>Feature 24</b></td><td><b>Feature 25</b></td><td><b>Feature 26</b></td><td><b>Feature 27</b></td><td><b>Feature 28</b></td><td><b>Feature 29</b></td></tr><tr><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature0.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature1.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature2.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature3.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature4.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature5.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature6.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature7.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature8.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature9.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature10.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature11.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature12.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature13.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature14.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature15.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature16.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature17.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature18.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature19.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature20.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature21.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature22.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature23.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature24.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature25.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature26.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature27.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature28.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515014923/wordclouds/Wordcloud_Feature29.png" width="400" height="200"></td></tr><tr><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.084</b>
&emsp;&emsp;&emsp;- positive = -0.039</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.443
<b>&emsp;&emsp;&emsp;- positive = -0.198</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.135
<b>&emsp;&emsp;&emsp;- positive = 0.137</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = 0.026
<b>&emsp;&emsp;&emsp;- positive = 0.136</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.244
<b>&emsp;&emsp;&emsp;- positive = -0.100</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.073
<b>&emsp;&emsp;&emsp;- positive = 0.440</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.292
<b>&emsp;&emsp;&emsp;- positive = 0.086</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.067
<b>&emsp;&emsp;&emsp;- positive = -0.025</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.278</b>
&emsp;&emsp;&emsp;- positive = -0.020</td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.385</b>
&emsp;&emsp;&emsp;- positive = 0.209</td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.427</b>
&emsp;&emsp;&emsp;- positive = 0.058</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.318
<b>&emsp;&emsp;&emsp;- positive = 0.125</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.059</b>
&emsp;&emsp;&emsp;- positive = -0.431</td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.438</b>
&emsp;&emsp;&emsp;- positive = -0.388</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.171
<b>&emsp;&emsp;&emsp;- positive = 0.045</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.371
<b>&emsp;&emsp;&emsp;- positive = 0.289</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = -0.121</b>
&emsp;&emsp;&emsp;- positive = -0.307</td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.436</b>
&emsp;&emsp;&emsp;- positive = -0.174</td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = -0.014</b>
&emsp;&emsp;&emsp;- positive = -0.393</td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.061</b>
&emsp;&emsp;&emsp;- positive = -0.134</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.277
<b>&emsp;&emsp;&emsp;- positive = 0.003</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.416</b>
&emsp;&emsp;&emsp;- positive = -0.425</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.423
<b>&emsp;&emsp;&emsp;- positive = -0.179</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.141</b>
&emsp;&emsp;&emsp;- positive = -0.326</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.219
<b>&emsp;&emsp;&emsp;- positive = 0.315</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = -0.064</b>
&emsp;&emsp;&emsp;- positive = -0.316</td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.492</b>
&emsp;&emsp;&emsp;- positive = -0.066</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.323
<b>&emsp;&emsp;&emsp;- positive = 0.418</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.277</b>
&emsp;&emsp;&emsp;- positive = -0.406</td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.229</b>
&emsp;&emsp;&emsp;- positive = -0.306</td></tr><tr><td><b>&emsp;&emsp;Human answers</b>:
<b>&emsp;&emsp;&emsp;- mostly negative = 4</b>
&emsp;&emsp;&emsp;- partially negative = 3
&emsp;&emsp;&emsp;- neither = 3
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 0
<b>&emsp;&emsp;&emsp;- mostly positive = 10</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 2
<b>&emsp;&emsp;&emsp;- partially positive = 4</b>
<b>&emsp;&emsp;&emsp;- mostly positive = 4</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 1
&emsp;&emsp;&emsp;- partially positive = 1
<b>&emsp;&emsp;&emsp;- mostly positive = 8</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
<b>&emsp;&emsp;&emsp;- neither = 5</b>
&emsp;&emsp;&emsp;- partially positive = 2
&emsp;&emsp;&emsp;- mostly positive = 3</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
<b>&emsp;&emsp;&emsp;- neither = 5</b>
&emsp;&emsp;&emsp;- partially positive = 3
&emsp;&emsp;&emsp;- mostly positive = 2</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 1
<b>&emsp;&emsp;&emsp;- mostly positive = 9</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
<b>&emsp;&emsp;&emsp;- neither = 7</b>
&emsp;&emsp;&emsp;- partially positive = 2
&emsp;&emsp;&emsp;- mostly positive = 1</td><td><b>&emsp;&emsp;Human answers</b>:
<b>&emsp;&emsp;&emsp;- mostly negative = 9</b>
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 1</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
<b>&emsp;&emsp;&emsp;- neither = 6</b>
&emsp;&emsp;&emsp;- partially positive = 1
&emsp;&emsp;&emsp;- mostly positive = 3</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 2
&emsp;&emsp;&emsp;- partially negative = 3
<b>&emsp;&emsp;&emsp;- neither = 4</b>
&emsp;&emsp;&emsp;- partially positive = 1
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 4
<b>&emsp;&emsp;&emsp;- mostly positive = 6</b></td><td><b>&emsp;&emsp;Human answers</b>:
<b>&emsp;&emsp;&emsp;- mostly negative = 10</b>
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 1
&emsp;&emsp;&emsp;- partially negative = 3
<b>&emsp;&emsp;&emsp;- neither = 6</b>
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 1
<b>&emsp;&emsp;&emsp;- mostly positive = 9</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 2
<b>&emsp;&emsp;&emsp;- mostly positive = 8</b></td><td><b>&emsp;&emsp;Human answers</b>:
<b>&emsp;&emsp;&emsp;- mostly negative = 7</b>
&emsp;&emsp;&emsp;- partially negative = 2
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 1</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 2
<b>&emsp;&emsp;&emsp;- neither = 5</b>
&emsp;&emsp;&emsp;- partially positive = 3
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
<b>&emsp;&emsp;&emsp;- mostly negative = 7</b>
&emsp;&emsp;&emsp;- partially negative = 2
&emsp;&emsp;&emsp;- neither = 1
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
<b>&emsp;&emsp;&emsp;- mostly negative = 7</b>
&emsp;&emsp;&emsp;- partially negative = 3
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 3
<b>&emsp;&emsp;&emsp;- partially positive = 4</b>
&emsp;&emsp;&emsp;- mostly positive = 3</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 3
<b>&emsp;&emsp;&emsp;- partially negative = 4</b>
&emsp;&emsp;&emsp;- neither = 2
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 1</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 1
&emsp;&emsp;&emsp;- neither = 1
&emsp;&emsp;&emsp;- partially positive = 3
<b>&emsp;&emsp;&emsp;- mostly positive = 5</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 2
&emsp;&emsp;&emsp;- partially negative = 2
<b>&emsp;&emsp;&emsp;- neither = 4</b>
&emsp;&emsp;&emsp;- partially positive = 1
&emsp;&emsp;&emsp;- mostly positive = 1</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 2
<b>&emsp;&emsp;&emsp;- mostly positive = 8</b></td><td><b>&emsp;&emsp;Human answers</b>:
<b>&emsp;&emsp;&emsp;- mostly negative = 10</b>
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
<b>&emsp;&emsp;&emsp;- mostly negative = 9</b>
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 1</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 1
&emsp;&emsp;&emsp;- partially positive = 3
<b>&emsp;&emsp;&emsp;- mostly positive = 6</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 3
<b>&emsp;&emsp;&emsp;- partially negative = 5</b>
&emsp;&emsp;&emsp;- neither = 1
&emsp;&emsp;&emsp;- partially positive = 1
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 2
<b>&emsp;&emsp;&emsp;- neither = 7</b>
&emsp;&emsp;&emsp;- partially positive = 1
&emsp;&emsp;&emsp;- mostly positive = 0</td></tr><tr><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.1
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 2.0
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.2
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.7
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.8
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.7
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.9
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.4
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.6
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: -0.7
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.6
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.6
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 2.0
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.5
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.9
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.8
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.4
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: -0.1
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.6
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.7
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.0
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.8
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.2
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.3
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.8
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 2.0
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.6
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.5
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.0
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.1
&emsp;&emsp;&emsp;- <b>Rank: C</b></td></tr></tbody></table>

### Model 2: YelpSmall500_CNN_20200515024859

<table><tbody><tr class="center-row"><td><b>Feature 0</b></td><td><b>Feature 1</b></td><td><b>Feature 2</b></td><td><b>Feature 3</b></td><td><b>Feature 4</b></td><td><b>Feature 5</b></td><td><b>Feature 6</b></td><td><b>Feature 7</b></td><td><b>Feature 8</b></td><td><b>Feature 9</b></td><td><b>Feature 10</b></td><td><b>Feature 11</b></td><td><b>Feature 12</b></td><td><b>Feature 13</b></td><td><b>Feature 14</b></td><td><b>Feature 15</b></td><td><b>Feature 16</b></td><td><b>Feature 17</b></td><td><b>Feature 18</b></td><td><b>Feature 19</b></td><td><b>Feature 20</b></td><td><b>Feature 21</b></td><td><b>Feature 22</b></td><td><b>Feature 23</b></td><td><b>Feature 24</b></td><td><b>Feature 25</b></td><td><b>Feature 26</b></td><td><b>Feature 27</b></td><td><b>Feature 28</b></td><td><b>Feature 29</b></td></tr><tr><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature0.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature1.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature2.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature3.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature4.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature5.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature6.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature7.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature8.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature9.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature10.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature11.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature12.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature13.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature14.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature15.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature16.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature17.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature18.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature19.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature20.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature21.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature22.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature23.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature24.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature25.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature26.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature27.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature28.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515024859/wordclouds/Wordcloud_Feature29.png" width="400" height="200"></td></tr><tr><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.330
<b>&emsp;&emsp;&emsp;- positive = -0.053</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = 0.050
<b>&emsp;&emsp;&emsp;- positive = 0.270</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.462</b>
&emsp;&emsp;&emsp;- positive = -0.433</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.362
<b>&emsp;&emsp;&emsp;- positive = 0.439</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.396</b>
&emsp;&emsp;&emsp;- positive = -0.229</td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = -0.092</b>
&emsp;&emsp;&emsp;- positive = -0.434</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.175
<b>&emsp;&emsp;&emsp;- positive = -0.014</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.285
<b>&emsp;&emsp;&emsp;- positive = -0.199</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.439
<b>&emsp;&emsp;&emsp;- positive = -0.127</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.075
<b>&emsp;&emsp;&emsp;- positive = 0.063</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.137</b>
&emsp;&emsp;&emsp;- positive = -0.015</td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.183</b>
&emsp;&emsp;&emsp;- positive = 0.035</td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = -0.120</b>
&emsp;&emsp;&emsp;- positive = -0.403</td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.415</b>
&emsp;&emsp;&emsp;- positive = -0.016</td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.441</b>
&emsp;&emsp;&emsp;- positive = -0.015</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = 0.121
<b>&emsp;&emsp;&emsp;- positive = 0.438</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = -0.138</b>
&emsp;&emsp;&emsp;- positive = -0.375</td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.163</b>
&emsp;&emsp;&emsp;- positive = -0.248</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.052
<b>&emsp;&emsp;&emsp;- positive = 0.112</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = 0.031
<b>&emsp;&emsp;&emsp;- positive = 0.194</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.108
<b>&emsp;&emsp;&emsp;- positive = 0.031</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.418
<b>&emsp;&emsp;&emsp;- positive = -0.071</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.065
<b>&emsp;&emsp;&emsp;- positive = 0.046</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = 0.323
<b>&emsp;&emsp;&emsp;- positive = 0.478</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.205</b>
&emsp;&emsp;&emsp;- positive = -0.279</td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.151</b>
&emsp;&emsp;&emsp;- positive = -0.085</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.381
<b>&emsp;&emsp;&emsp;- positive = 0.137</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.375</b>
&emsp;&emsp;&emsp;- positive = -0.242</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.007
<b>&emsp;&emsp;&emsp;- positive = 0.308</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.064</b>
&emsp;&emsp;&emsp;- positive = -0.452</td></tr><tr><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
<b>&emsp;&emsp;&emsp;- neither = 5</b>
&emsp;&emsp;&emsp;- partially positive = 3
&emsp;&emsp;&emsp;- mostly positive = 2</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 2
<b>&emsp;&emsp;&emsp;- partially positive = 6</b>
&emsp;&emsp;&emsp;- mostly positive = 2</td><td><b>&emsp;&emsp;Human answers</b>:
<b>&emsp;&emsp;&emsp;- mostly negative = 7</b>
&emsp;&emsp;&emsp;- partially negative = 1
&emsp;&emsp;&emsp;- neither = 2
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 2
<b>&emsp;&emsp;&emsp;- mostly positive = 8</b></td><td><b>&emsp;&emsp;Human answers</b>:
<b>&emsp;&emsp;&emsp;- mostly negative = 8</b>
&emsp;&emsp;&emsp;- partially negative = 2
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
<b>&emsp;&emsp;&emsp;- partially negative = 7</b>
&emsp;&emsp;&emsp;- neither = 1
&emsp;&emsp;&emsp;- partially positive = 2
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 1
<b>&emsp;&emsp;&emsp;- partially positive = 5</b>
&emsp;&emsp;&emsp;- mostly positive = 4</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 1
&emsp;&emsp;&emsp;- partially positive = 3
<b>&emsp;&emsp;&emsp;- mostly positive = 6</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 1
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 3
&emsp;&emsp;&emsp;- partially positive = 1
<b>&emsp;&emsp;&emsp;- mostly positive = 5</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 3
<b>&emsp;&emsp;&emsp;- partially positive = 4</b>
&emsp;&emsp;&emsp;- mostly positive = 3</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 1
<b>&emsp;&emsp;&emsp;- neither = 7</b>
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 2</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 3
<b>&emsp;&emsp;&emsp;- partially negative = 6</b>
&emsp;&emsp;&emsp;- neither = 1
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
<b>&emsp;&emsp;&emsp;- neither = 8</b>
&emsp;&emsp;&emsp;- partially positive = 2
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 3
<b>&emsp;&emsp;&emsp;- neither = 5</b>
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 2</td><td><b>&emsp;&emsp;Human answers</b>:
<b>&emsp;&emsp;&emsp;- mostly negative = 6</b>
&emsp;&emsp;&emsp;- partially negative = 1
&emsp;&emsp;&emsp;- neither = 2
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 1</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 0
<b>&emsp;&emsp;&emsp;- mostly positive = 10</b></td><td><b>&emsp;&emsp;Human answers</b>:
<b>&emsp;&emsp;&emsp;- mostly negative = 5</b>
&emsp;&emsp;&emsp;- partially negative = 3
&emsp;&emsp;&emsp;- neither = 2
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
<b>&emsp;&emsp;&emsp;- mostly negative = 9</b>
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 1
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 2
<b>&emsp;&emsp;&emsp;- mostly positive = 8</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 3
<b>&emsp;&emsp;&emsp;- partially positive = 6</b>
&emsp;&emsp;&emsp;- mostly positive = 1</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 3
<b>&emsp;&emsp;&emsp;- mostly positive = 7</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 2
<b>&emsp;&emsp;&emsp;- mostly positive = 8</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 1
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 1
<b>&emsp;&emsp;&emsp;- mostly positive = 8</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 1
&emsp;&emsp;&emsp;- partially positive = 4
<b>&emsp;&emsp;&emsp;- mostly positive = 5</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 1
<b>&emsp;&emsp;&emsp;- neither = 9</b>
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
<b>&emsp;&emsp;&emsp;- mostly negative = 8</b>
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 2
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 3
<b>&emsp;&emsp;&emsp;- mostly positive = 7</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 3
&emsp;&emsp;&emsp;- partially negative = 3
<b>&emsp;&emsp;&emsp;- neither = 4</b>
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 1
&emsp;&emsp;&emsp;- partially positive = 1
<b>&emsp;&emsp;&emsp;- mostly positive = 8</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 1
<b>&emsp;&emsp;&emsp;- neither = 9</b>
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td></tr><tr><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.7
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.0
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.5
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.8
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.8
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.5
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.3
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.5
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.9
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.0
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: -0.3
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.2
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: -0.2
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: -0.1
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.1
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 2.0
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.3
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.8
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.8
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.8
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.7
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.8
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.6
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.4
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.1
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.6
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.7
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.9
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.7
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.1
&emsp;&emsp;&emsp;- <b>Rank: C</b></td></tr></tbody></table>

### Model 3: YelpSmall500_CNN_20200515025212

<table><tbody><tr class="center-row"><td><b>Feature 0</b></td><td><b>Feature 1</b></td><td><b>Feature 2</b></td><td><b>Feature 3</b></td><td><b>Feature 4</b></td><td><b>Feature 5</b></td><td><b>Feature 6</b></td><td><b>Feature 7</b></td><td><b>Feature 8</b></td><td><b>Feature 9</b></td><td><b>Feature 10</b></td><td><b>Feature 11</b></td><td><b>Feature 12</b></td><td><b>Feature 13</b></td><td><b>Feature 14</b></td><td><b>Feature 15</b></td><td><b>Feature 16</b></td><td><b>Feature 17</b></td><td><b>Feature 18</b></td><td><b>Feature 19</b></td><td><b>Feature 20</b></td><td><b>Feature 21</b></td><td><b>Feature 22</b></td><td><b>Feature 23</b></td><td><b>Feature 24</b></td><td><b>Feature 25</b></td><td><b>Feature 26</b></td><td><b>Feature 27</b></td><td><b>Feature 28</b></td><td><b>Feature 29</b></td></tr><tr><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature0.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature1.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature2.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature3.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature4.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature5.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature6.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature7.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature8.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature9.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature10.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature11.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature12.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature13.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature14.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature15.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature16.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature17.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature18.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature19.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature20.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature21.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature22.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature23.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature24.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature25.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature26.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature27.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature28.png" width="400" height="200"></td><td><img src="https://www.doc.ic.ac.uk/~pl1515/files/YelpSmall500_CNN_20200515025212/wordclouds/Wordcloud_Feature29.png" width="400" height="200"></td></tr><tr><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.308
<b>&emsp;&emsp;&emsp;- positive = -0.163</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.391
<b>&emsp;&emsp;&emsp;- positive = -0.325</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.385</b>
&emsp;&emsp;&emsp;- positive = 0.295</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.169
<b>&emsp;&emsp;&emsp;- positive = -0.152</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = 0.122
<b>&emsp;&emsp;&emsp;- positive = 0.324</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = 0.027
<b>&emsp;&emsp;&emsp;- positive = 0.344</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.119
<b>&emsp;&emsp;&emsp;- positive = 0.153</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = 0.327
<b>&emsp;&emsp;&emsp;- positive = 0.422</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.083</b>
&emsp;&emsp;&emsp;- positive = -0.277</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.397
<b>&emsp;&emsp;&emsp;- positive = 0.183</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.361
<b>&emsp;&emsp;&emsp;- positive = 0.285</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = -0.080</b>
&emsp;&emsp;&emsp;- positive = -0.343</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.300
<b>&emsp;&emsp;&emsp;- positive = 0.260</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.044</b>
&emsp;&emsp;&emsp;- positive = -0.227</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.032
<b>&emsp;&emsp;&emsp;- positive = 0.081</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.431</b>
&emsp;&emsp;&emsp;- positive = -0.130</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = 0.146
<b>&emsp;&emsp;&emsp;- positive = 0.266</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.271</b>
&emsp;&emsp;&emsp;- positive = -0.058</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.429
<b>&emsp;&emsp;&emsp;- positive = 0.046</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.299</b>
&emsp;&emsp;&emsp;- positive = -0.237</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.422
<b>&emsp;&emsp;&emsp;- positive = 0.367</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = -0.320</b>
&emsp;&emsp;&emsp;- positive = -0.432</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.245
<b>&emsp;&emsp;&emsp;- positive = -0.168</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.022</b>
&emsp;&emsp;&emsp;- positive = -0.387</td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = -0.117</b>
&emsp;&emsp;&emsp;- positive = -0.152</td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.310</b>
&emsp;&emsp;&emsp;- positive = -0.222</td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = -0.367
<b>&emsp;&emsp;&emsp;- positive = 0.127</b></td><td>&emsp;&emsp;<b>Model weights</b>:
&emsp;&emsp;&emsp;- negative = 0.150
<b>&emsp;&emsp;&emsp;- positive = 0.332</b></td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.149</b>
&emsp;&emsp;&emsp;- positive = -0.380</td><td>&emsp;&emsp;<b>Model weights</b>:
<b>&emsp;&emsp;&emsp;- negative = 0.205</b>
&emsp;&emsp;&emsp;- positive = 0.154</td></tr><tr><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
<b>&emsp;&emsp;&emsp;- partially negative = 3</b>
<b>&emsp;&emsp;&emsp;- neither = 3</b>
&emsp;&emsp;&emsp;- partially positive = 2
&emsp;&emsp;&emsp;- mostly positive = 2</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
<b>&emsp;&emsp;&emsp;- neither = 9</b>
&emsp;&emsp;&emsp;- partially positive = 1
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
<b>&emsp;&emsp;&emsp;- neither = 7</b>
&emsp;&emsp;&emsp;- partially positive = 2
&emsp;&emsp;&emsp;- mostly positive = 1</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 2
&emsp;&emsp;&emsp;- partially positive = 3
<b>&emsp;&emsp;&emsp;- mostly positive = 5</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
<b>&emsp;&emsp;&emsp;- neither = 8</b>
&emsp;&emsp;&emsp;- partially positive = 2
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
<b>&emsp;&emsp;&emsp;- neither = 6</b>
&emsp;&emsp;&emsp;- partially positive = 3
&emsp;&emsp;&emsp;- mostly positive = 1</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 2
<b>&emsp;&emsp;&emsp;- mostly positive = 8</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 1
<b>&emsp;&emsp;&emsp;- neither = 5</b>
&emsp;&emsp;&emsp;- partially positive = 4
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
<b>&emsp;&emsp;&emsp;- neither = 8</b>
&emsp;&emsp;&emsp;- partially positive = 2
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 4
<b>&emsp;&emsp;&emsp;- neither = 5</b>
&emsp;&emsp;&emsp;- partially positive = 1
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
&emsp;&emsp;&emsp;- partially positive = 4
<b>&emsp;&emsp;&emsp;- mostly positive = 6</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
<b>&emsp;&emsp;&emsp;- neither = 9</b>
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 1</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
<b>&emsp;&emsp;&emsp;- neither = 7</b>
&emsp;&emsp;&emsp;- partially positive = 2
&emsp;&emsp;&emsp;- mostly positive = 1</td><td><b>&emsp;&emsp;Human answers</b>:
<b>&emsp;&emsp;&emsp;- mostly negative = 7</b>
&emsp;&emsp;&emsp;- partially negative = 2
&emsp;&emsp;&emsp;- neither = 1
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 4
<b>&emsp;&emsp;&emsp;- partially positive = 5</b>
&emsp;&emsp;&emsp;- mostly positive = 1</td><td><b>&emsp;&emsp;Human answers</b>:
<b>&emsp;&emsp;&emsp;- mostly negative = 6</b>
&emsp;&emsp;&emsp;- partially negative = 3
&emsp;&emsp;&emsp;- neither = 1
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 1
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 0
<b>&emsp;&emsp;&emsp;- partially positive = 5</b>
&emsp;&emsp;&emsp;- mostly positive = 4</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 4
<b>&emsp;&emsp;&emsp;- neither = 5</b>
&emsp;&emsp;&emsp;- partially positive = 1
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 1
&emsp;&emsp;&emsp;- neither = 2
<b>&emsp;&emsp;&emsp;- partially positive = 5</b>
&emsp;&emsp;&emsp;- mostly positive = 2</td><td><b>&emsp;&emsp;Human answers</b>:
<b>&emsp;&emsp;&emsp;- mostly negative = 6</b>
&emsp;&emsp;&emsp;- partially negative = 2
&emsp;&emsp;&emsp;- neither = 2
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
<b>&emsp;&emsp;&emsp;- neither = 8</b>
&emsp;&emsp;&emsp;- partially positive = 2
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 3
&emsp;&emsp;&emsp;- partially negative = 1
<b>&emsp;&emsp;&emsp;- neither = 4</b>
&emsp;&emsp;&emsp;- partially positive = 2
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 1
<b>&emsp;&emsp;&emsp;- neither = 5</b>
&emsp;&emsp;&emsp;- partially positive = 3
&emsp;&emsp;&emsp;- mostly positive = 1</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 1
<b>&emsp;&emsp;&emsp;- partially negative = 6</b>
&emsp;&emsp;&emsp;- neither = 1
&emsp;&emsp;&emsp;- partially positive = 2
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 2
<b>&emsp;&emsp;&emsp;- neither = 5</b>
&emsp;&emsp;&emsp;- partially positive = 3
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 2
<b>&emsp;&emsp;&emsp;- partially negative = 4</b>
<b>&emsp;&emsp;&emsp;- neither = 4</b>
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
&emsp;&emsp;&emsp;- neither = 1
&emsp;&emsp;&emsp;- partially positive = 4
<b>&emsp;&emsp;&emsp;- mostly positive = 5</b></td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
&emsp;&emsp;&emsp;- partially negative = 0
<b>&emsp;&emsp;&emsp;- neither = 7</b>
&emsp;&emsp;&emsp;- partially positive = 2
&emsp;&emsp;&emsp;- mostly positive = 1</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 0
<b>&emsp;&emsp;&emsp;- partially negative = 7</b>
&emsp;&emsp;&emsp;- neither = 2
&emsp;&emsp;&emsp;- partially positive = 1
&emsp;&emsp;&emsp;- mostly positive = 0</td><td><b>&emsp;&emsp;Human answers</b>:
&emsp;&emsp;&emsp;- mostly negative = 1
&emsp;&emsp;&emsp;- partially negative = 4
<b>&emsp;&emsp;&emsp;- neither = 5</b>
&emsp;&emsp;&emsp;- partially positive = 0
&emsp;&emsp;&emsp;- mostly positive = 0</td></tr><tr><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.3
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.1
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: -0.4
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.3
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.2
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.5
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.8
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.3
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: -0.2
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: -0.3
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.6
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: -0.2
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.4
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.6
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.7
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.5
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.1
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.3
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.8
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.4
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.2
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.5
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.4
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.6
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: -0.1
&emsp;&emsp;&emsp;- <b>Rank: C</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.8
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 1.4
&emsp;&emsp;&emsp;- <b>Rank: A</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.4
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.6
&emsp;&emsp;&emsp;- <b>Rank: B</b></td><td>&emsp;&emsp;<b>Summary:</b>
&emsp;&emsp;&emsp;- Average score: 0.6
&emsp;&emsp;&emsp;- <b>Rank: B</b></td></tr></tbody></table>

<hr>

## Results
![Result table](../figures/table_1A.PNG)
*Results (Average ± SD) of Experiment 1: Yelp, CNNs; Boldface numbers are the best scores in the columns. They are further underlined if they are significantly better than the scores of all the other models (based on approximate randomization test with α = 0.05)*

<hr>

## Downloads
- Models (Available soon)
- [Wordclouds and annotations](https://drive.google.com/file/d/1k7GmoT51Lcqx7x6nkY56VaegVSK0UNIT/view?usp=sharing)
- The dataset of this experiment as well as other experiments can be downloaded [here](https://drive.google.com/file/d/1yKgNqbli_loWakg0NpZkmfi3jBj_N7FK/view?usp=sharing).
