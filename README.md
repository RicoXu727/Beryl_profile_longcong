# Beryl_profile_longcong
Beryl Consulting data scientist project


# Clone repositories

```
git clone 'https://github.com/RicoXu727/Beryl_profile_longcong.git'
```

Install required packages
```
pip install -r requirements.txt
```

# Connect to Twitter database via API

Example of one scraped data record
```
{"created_at": "Tue Jan 10 17:38:33 +0000 2023", 
"id": 1612866496920981504, 
"id_str": "1612866496920981504", 
"full_text": "Intel Capital's Managing Director &amp; Head of Investment Operations @jenny_ard sits on the board of directors for Fabric8Labs &amp; is proud to work with the team to support their unique printing process that disrupts traditional high-precision metal manufacturing methods.", "truncated": false, "display_text_range": [0, 275], 
"entities": {"hashtags": [], "symbols": [], "user_mentions": [{"screen_name": "jenny_ard", "name": "Jennifer Ard", "id": 4073475314, "id_str": "4073475314", "indices": [70, 80]}], "urls": []}, "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>", "in_reply_to_status_id": 1612866495536836609, "in_reply_to_status_id_str": "1612866495536836609", "in_reply_to_user_id": 27994823, "in_reply_to_user_id_str": "27994823", "in_reply_to_screen_name": "intelcapital", "user": {"id": 27994823, "id_str": "27994823", "name": "Intel Capital", "screen_name": "intelcapital", "location": "Santa Clara, CA", "description": "A force multiplier for early stage startups - inspiring and investing in the future of compute.", "url": "https://t.co/RmwMrNPuPq", "entities": {"url": {"urls": [{"url": "https://t.co/RmwMrNPuPq", "expanded_url": "http://www.intelcapital.com", "display_url": "intelcapital.com", "indices": [0, 23]}]}, "description": {"urls": []}}, "protected": false, "followers_count": 29130, "friends_count": 1102, "listed_count": 1130, "created_at": "Tue Mar 31 23:33:16 +0000 2009", "favourites_count": 1758, "utc_offset": null, "time_zone": null, "geo_enabled": true, "verified": true, "statuses_count": 5828, "lang": null, "contributors_enabled": false, "is_translator": false, "is_translation_enabled": false, "profile_background_color": "028CD7", "profile_background_image_url": "http://abs.twimg.com/images/themes/theme4/bg.gif", "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme4/bg.gif", "profile_background_tile": false, "profile_image_url": "http://pbs.twimg.com/profile_images/1468279253242314752/Afa7DCr7_normal.jpg", 
"profile_image_url_https": "https://pbs.twimg.com/profile_images/1468279253242314752/Afa7DCr7_normal.jpg", 
"profile_banner_url": "https://pbs.twimg.com/profile_banners/27994823/1638900028", "profile_link_color": "0099B9", "profile_sidebar_border_color": "FFFFFF", "profile_sidebar_fill_color": "F2F2F2", "profile_text_color": "000000", "profile_use_background_image": true, "has_extended_profile": false, "default_profile": false, "default_profile_image": false, "following": false, "follow_request_sent": false, 
"notifications": false, "translator_type": "none", "withheld_in_countries": []}, "geo": null, 
"coordinates": null, "place": null, "contributors": null, "is_quote_status": false, 
"retweet_count": 0, "favorite_count": 0, "favorited": false, "retweeted": false, "lang": "en"}
```

# Collect and monitor the content they share

Use the poll function to update the collected data each time a request is sent.


# Deal with raw data

After getting the data, by getting all the keys in the json, I filtered out some attributes that I thought were useful for the study and directly removed some redundant variables. Then write to csv file line by line. Here is the attributes I choose and their explanation respectively:
| Attribute | Explanation |
| --------- | ----------- |
| created_at | Time created |
| user | User object |
| full_text | Tweet text |
| hashtags | List of hashtags used in the tweet |
| people_mentions | List of users mentioned in the tweet |
| in_reply_to_status_id | If the represented tweet is a reply, this field will contain the integer representation of the original tweet’s ID |
| retweet_count | Number of times this tweet has been retweeted |
| retweeted | Boolean indicating whether this tweet has been retweeted by the authenticating user |
| favorite_count | Indicates approximately how many times this tweet has been liked by Twitter users |
| favorited | Boolean indicating whether this tweet has been liked by the authenticating user |


To **evaluate the quality of the data**, I use **BART** (Bidirectional and Auto-Regressive Transformers) language model which is a denoising self-encoder designed for pre-training sequence-to-sequence models proposed by Facebook. This model can find typos, jumbled characters and correct them. I compare the sentences output by the model with the original text and use **ROUGE** (Recall-Oriented Understudy for Gisting Evaluation) to calculate the deviation between them. If the deviation is large, it means that the original text has low quality data, and if the deviation is small, it means that the data found from Twitter is of high quality.

Take Intel Capital data as an example:
The ROUGE values are around 0.97 which shows the data scraped from twitter have **high quality**, in our next analysis, we can directly use the data generated from BART model!

# Data Integrity Testing

Before we feed our data to the ML models, we should test the level of missing value. Simply use the pachage from pandas, the result shows there are no missing values except for in_reply_to_user_id, but we can't remove this column, which is very useful to discover the interaction between intel capital and other users. The best thing to do is to fill all this column with 0.

# ML Model 1 : Topic modeling (LDA): 

The LDS identify topics by the frequency of words and phrases in the Twitter data to understand the topics and industry trends that companies focus on.

Firstly import the CSV into pandas form and then perform some necessary conversions on the 'text' column that we want to analyze.

1. Remove punctuation like '[#,\.!?@]'

2. Convert the text to lowercase

3. **The most important one** : delete all default urls at the end of each records 

Let's first observe the results of data processing using WordCloud. Not bad, but the words that appear in the word cloud don't really represent intel capital's investment areas or areas of interest.

BERT is a powerful language model that can capture the context and meaning of words based on their surrounding words, as well as their position in a sentence or a document. By leveraging the power of BERT, we can enhance the quality of topic modeling by incorporating the semantic information of words.

From the results, it seems that the model is somewhat overtrained and the inclusion of the BERT model seems a bit trivial.

Using the method without BART, I built a model with 10 topics where each topic is a combination of keywords, and each keyword contributes a certain weightage to the topic. The textual result is not very intuitive and is easier to observe when we visualize it by using pyLDAvis package.  We can see that **Immuta, Ai,amp** are some of the most frequently occurring keywords in the text. This is strong evidence that intel capital cares deeply about the technology market. Immuta and Amp'd Mobile are both software development companies, and intel capital has tweeted about them several times.


# ML Model 2 : Entity identification : 

To know some of the most frequent company names, names of people or geographical locations in interl capital's tweets, we can use Entity identification to analyze the text, specificly, Named-Entity-Recognition (NER). The model is able to accept a wide range of textual inputs, so some good results can be obtained without having to process the textual data too much. But we still have to remove the default urls at the end of the text. 

However, we can clearly find a small flaw in this model, which does not distinguish well between corporate organizations and human names. Even if it does not give us a clear classification, we can still get useful hints from the model results. For example, Sunil Kurkure is often mentioned in interl capital, which is the senior management of interl capital as well as Analytics CEO Andrea Remyn Stone at Alkymi which may imply that intel capital are very concerned Alkymi or already have a partnership with it.


# References

BART model:
```
https://towardsdatascience.com/bart-for-paraphrasing-with-simple-transformers-7c9ea3dfdd8c
```

ROUGE metric:
```
https://www.freecodecamp.org/news/what-is-rouge-and-how-it-works-for-evaluation-of-summaries-e059fb8ac840/
```

Topic modeling(LDA): 

```
https://towardsdatascience.com/end-to-end-topic-modeling-in-python-latent-dirichlet-allocation-lda-35ce4ed6b3e0
```

Named-Entity-Recognition (NER) on Twitter with Bi-directional LSTM with tensorflow in python : 

```
https://sandipanweb.wordpress.com/2020/08/30/named-entity-recognition-ner-on-twitter-with-bi-directional-lstm-with-tensorflow-in-python/
```
