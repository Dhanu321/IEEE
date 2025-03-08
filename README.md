# Data Release for ArPFN Dataset 
The directory contains the data used in the paper [**_Detecting Users Prone to Spread Fake News on Arabic Twitter_**](http://www.lrec-conf.org/proceedings/lrec2022/workshops/OSACT/pdf/2022.osact-1.2.pdf) published in The 5th Workshop on Open-Source Arabic Corpora and Processing Tools (OSACT5). To maintain user privacy, we refrain from publishing the user ids or the text of the users’ tweets. In this data release, the field _user_id_ is a sequence number used to represent the user. 

## Directory content 
- **Users.csv**: csv file containing the following fields:
   - **user_id**: identifier representing the user 
   - **N_False**: Number of False tweets and retweets made by the user
   - **N_True**: Number of True tweets and retweets made by the user
### Features 
Directory containing all feature categories used in our experiments, the content of the feature files are summarized below. 

- **textual_features.csv**: csv file containing textual features used in our experiments. It contains the following fields:
   - **user_id**: identifier representing the user
   - **tri_grams**: vector representing character tri-grams of the user’s recent 100 tweets

- **profile_features.csv**: csv file containing profile features used in our experiments. It contains the following fields:
   - **user_id** (Integer): identifier representing the user 
   - **default_profile** (Boolean): If the user has changed the default theme or background of their profile or not
   - **verified** (Boolean): If the user has a verified account or not
   - **followers_count** (Integer): Number of followers the account has
   - **following_count** (Integer): Number of users that the account is following
   - **favorites_count** (Integer): Number of tweets that were liked by the user
   - **listed_count** (Integer): Number of lists the user has been added to
   - **statuses_count** (Integer): Number of tweets posted by the user
   - **tweet_frequency** (Float): Frequency of the user’s tweets, calculated as tweets count divided by account age in months
   - **follower_growth_rate** (Float): Rate of followers growth, calculated as followers count divided by account age
   - **following_growth_rate** (Float): Rate of following growth, calculated as friends count divided by account age
   - **listed_growth_rate** (Float): Rate of lists growth, calculated as lists count divided by account age
   - **followers_following_ratio** (Float): Number of followers compared to following
   - **screen_name_length** (Integer): Number of characters in the user’s screen name
   - **digits_in_screen_name** (Integer): Number of digits in the user’s screen name
   - **name_length** (Integer): Number of characters in the name of the user
   - **digits_in_name** (Integer): Number of numerical digits in the name of the user
   - **description_length** (Integer): Number of characters in the user’s description (biography)

- **Statistical_features.csv**: csv file containing statistical features used in our experiments. It contains the following fields:
   - **hashtags_ratio**: Ratio of user tweets that contain hashtags
   - **hashtags_per_twt**: Average number of hashtags per tweet
   - **mentions_ratio**: Ratio of user tweets that contain mentions
   - **unique_mentions_number**: Number of unique mentions in user’s timeline
   - **replies_ratio**: Ratio of user tweets that are replies
   - **urls_ratio**: Ratio of user tweets that contain URLS
   - **media_ratio**: Ratio of user tweets that contain media such as images or videos
   - **RT_count**: Number of tweets that are retweets
   - **quoted_RT_ratio**: Ratio of user tweets that are quote retweets
   - **avg_engagement**: Average engagement of the user, computed as the average number of retweets and likes per tweet
   - **avg_days_between_tweets**: Average days between each two consecutive tweets. 

- **emotional_features.csv**: csv file containing emotional signals used in our experiments. It contains the user id and the raw emotional signal score for all emotions. [ASAD tool](https://asad.qcri.org/api) was used to derive the features. The emotions used are: 
   - anger
   - anticipation
   - disgust
   - fear
   - joy
   - love
   - optimism
   - pessimism
   - sadness
   - surprise
   - trust

### Reproducibility
Directory containing the data split used in our experiments and the code used to generate the results
- CV_folds: Directory containing user_id of users used in each fold of our experiments 
- train.py: Python file containnig the code used to reproduce the same results used in our paper

## Contact information 
Please contact the authors of the paper for any queries: 
- [Zien Sheikh Ali ](mailto:zs1407404@qu.edu.qa)
- [Abdulaziz Al-Ali](mailto:a.alali@qu.edu.qa)
- [Tamer Elsayed](mailto:telsayed@qu.edu.qa)

## Citation 
If you use ArPFN dataset, please cite our paper 

```
@inproceedings{ArPFN2022,
    title={Detecting Users Prone to Spread Fake News on Arabic Twitter},
    author={Sheikh Ali, Zien and Al-Ali, Abdulaziz and Elsayed, Tamer},
    booktitle={The 5th Workshop on Open-Source Arabic Corpora and Processing Tools},
    pages={},
    publisher = {European Language Resources Association},
    year={2022}}
```
