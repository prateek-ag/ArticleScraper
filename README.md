# Data Scraping from Online News Articles

This module was developed during my research project under Professor Margo Seltzer, during the summer of 2019.

The Article Scraper aims to automatically extract provenance information from online news articles, and to store the information in an easily retrievable manner. Using a combination of machine learning models, rule-based object recognition, and external libraries such as BeautifulSoup, Newspaper3k, and the StanfordNLP library, the article scraping module is able to automatically detect and identify important textual elements of a news article from its webpage. Information such as author, quotations (quote and attributed speaker), linked pages (URL and a categorical classification) and more is extracted from the article and written to an output file in JSON format. The module then utilizes the prov-cpl library to create and store provenance entities and the relationships between them.

An example of the JSON output file can be seen here:

```json
[
    {
        "url": "https://www.bbc.com/news/world-us-canada-48972327",
        "title": "Facebook 'to be fined $5bn over Cambridge Analytica scandal'",
        "authors": [],
        "publisher": "www.bbc.com",
        "publish_date": "",
        "text": "Media playback is unsupported on your device Media caption How the Facebook-Cambridge Analytica data scandal unfolded\n\nUS regulators have approved a record $5bn (£4bn) fine on Facebook to settle an investigation into data privacy violations, reports in US media say.\n\nThe Federal Trade Commission (FTC) has been investigating allegations that political consultancy Cambridge Analytica improperly obtained the data of up to 87 million Facebook users.\n\nThe settlement was approved by the FTC in a 3-2 vote, sources told US media.\n\nFacebook and the FTC told the BBC they had no comment on the reports.\n\nHow was the settlement reached?\n\nThe consumer protection agency the FTC began investigating Facebook in March 2018 following reports that Cambridge Analytica had accessed the data of tens of millions of its users.\n\nThe investigation focused on whether Facebook had violated a 2011 agreement under which it was required to clearly notify users and gain \"express consent\" to share their data.\n\nThe $5bn fine was approved by the FTC in a 3-2 vote which broke along party lines, with Republican commissioners in favour and Democrats opposed.\n\nThe New York Times reported that the Democrats wanted stricter limits on the firm, while other Democrats have criticised the fine as inadequate.\n\n\"With the FTC either unable or unwilling to put in place reasonable guardrails to ensure that user privacy and data are protected, it's time for Congress to act,\" US Senator Mark Warner said.\n\nThe fine still needs to be finalised by the Justice Department's civil division, and it is unclear how long this may take, the sources said.\n\nIf confirmed, it would be the largest fine ever levied by the FTC on a tech company.\n\nHowever, the amount falls in line with estimates by Facebook, which earlier this year said it was expecting a fine of up to $5bn.\n\nInvestors responded positively to the news, pushing Facebook shares up 1.8%.\n\nFacebook has been expecting this\n\nAnalysis by Dave Lee, BBC North America technology reporter in San Francisco\n\nFacebook had been expecting this. It told investors back in April that it had put aside most of the money, which means the firm won't feel much added financial strain from this penalty.\n\nWhat we don't yet know is what additional measures may be placed on the company, such as increased privacy oversight, or if there will be any personal repercussions for the company's chief executive, Mark Zuckerberg.\n\nThe settlement, which amounts to around one quarter of the company's yearly profit, will reignite criticism from those who say this amounts to little more than a slap on the wrist.\n\nWhat was the Cambridge Analytica scandal?\n\nCambridge Analytica was a British political consulting firm that had access to the data of millions of users, some of which was allegedly used to psychologically profile US voters and target them with material to help Donald Trump's 2016 presidential campaign.\n\nThe data was acquired via a quiz, which invited users to find out their personality type.\n\nAs was common with apps and games at that time, it was designed to harvest not only the user data of the person taking part in the quiz, but also the data of their friends.\n\nFacebook has said it believes the data of up to 87 million users was improperly shared with the now defunct consultancy.\n\nThe scandal sparked several investigations around the world.\n\nIn October, Facebook was fined £500,000 by the UK's data protection watchdog, which said the company had let a \"serious breach\" of the law take place.\n\nCanada's data watchdog earlier this year said Facebook had committed \"serious contraventions\" of its privacy laws.",
        "quotes": [
            [
                "With the FTC either unable or unwilling to put in place reasonable guardrails to ensure that user privacy and data are protected, it's time for Congress to act,",
                "Mark Warner",
                true
            ]
        ],
        "links": {
            "articles": [
                "https://www.bbc.co.uk/news/business-48045138",
                "https://www.nytimes.com/2019/07/12/technology/facebook-ftc-fine.html?action=click&module=Top%20Stories&pgtype=Homepage",
                "https://www.bbc.co.uk/news/technology-45976300"
            ],
            "gov_pgs": [],
            "unsure": []
        },
        "key_words": [
            "5bn",
            "data",
            "told",
            "scandal",
            "fine",
            "privacy",
            "ftc",
            "media",
            "facebook",
            "settlement",
            "users",
            "analytica",
            "cambridge",
            "fined"
        ]
    },
    {
        "url": "https://www.bbc.co.uk/news/business-48045138",
        "title": "Facebook sets aside $3bn for privacy probe",
        "authors": [],
        "publisher": "www.bbc.co.uk",
        "publish_date": "",
        "text": "Image copyright Reuters\n\nFacebook has said it will set aside $3bn (£2.3bn) to cover the potential costs of an investigation by US authorities into its privacy practices.\n\nWhile it has provided for a heavy toll from the investigation by the US Federal Trade Commission, the final cost could be $5bn, it said.\n\nThe social media giant also said total sales for the first three months of the year leapt 26% to $15.08bn, narrowly beating market expectations.\n\nMonthly users rose 8%, it said.\n\nThat rise takes the number of users to 2.38 billion.\n\n\"We had a good quarter and our business and community continued to grow,\" founder and chief executive Mark Zuckerberg said.\n\n\"We are focused on building out our privacy-focused vision for the future of social networking, and working collaboratively to address important issues around the internet.\"\n\nShares rise\n\nThe shares are up by nearly 40% in the year to date, far outperforming the broader market, and were up nearly 5% in late trading on Wall Street.\n\nFacebook is facing a probe over the Cambridge Analytica data scandal, however no findings have yet been published.\n\nFacebook was labelled \"morally bankrupt pathological liars\" by New Zealand's privacy commissioner this month after hosting a livestream of the Christchurch attacks that left 50 dead.\n\nIn an interview after the attacks, Mr Zuckerberg refused to commit to any changes to the platform's live technology, including a time delay on livestreams.\n\nFacebook, which owns Instagram, last week admitted that millions more Instagram users were affected by a security lapse than it had previously disclosed. It had mistakenly stored the passwords of hundreds of millions of users without encryption.",
        "quotes": [
            [
                "We had a good quarter and our business and community continued to grow,",
                "",
                true
            ],
            [
                "We are focused on building out our privacy-focused vision for the future of social networking, and working collaboratively to address important issues around the internet.",
                "",
                true
            ]
        ],
        "links": {
            "articles": [],
            "gov_pgs": [],
            "unsure": []
        },
        "key_words": [
            "investigation",
            "sets",
            "zuckerberg",
            "social",
            "attacks",
            "privacy",
            "facebook",
            "3bn",
            "millions",
            "instagram",
            "nearly",
            "probe",
            "market",
            "users",
            "aside"
        ]
    },
    {
        "url": "https://www.nytimes.com/2019/07/12/technology/facebook-ftc-fine.html?action=click&module=Top%20Stories&pgtype=Homepage",
        "title": "F.T.C. Approves Facebook Fine of About $5 Billion",
        "authors": [
            {
                "name": "Cecilia Kang",
                "link": null
            }
        ],
        "publisher": "www.nytimes.com",
        "publish_date": "2019-07-12",
        "text": "The Federal Trade Commission has approved a fine of roughly $5 billion against Facebook for mishandling users’ personal information, according to three people briefed on the vote, in what would be a landmark settlement that signals a newly aggressive stance by regulators toward the country’s most powerful technology companies.\n\nThe much-anticipated settlement still needs final approval in the coming weeks from the Justice Department, which rarely rejects settlements reached by the agency. It would be the biggest fine by far levied by the federal government against a technology company, easily eclipsing the $22 million imposed on Google in 2012. The size of the penalty underscored the rising frustration among Washington officials with how Silicon Valley giants collect, store and use people’s information.\n\nIt would also represent one of the most aggressive regulatory actions by the Trump administration, and a sign of the government’s willingness to punish one of the country’s biggest and most powerful companies. President Trump has dialed back regulations in many industries, but the Facebook settlement sets a new bar for privacy enforcement by United States officials, who have brought few cases against large technology companies.\n\nIn addition to the fine, Facebook agreed to more comprehensive oversight of how it handles user data, according to the people. But none of the conditions in the settlement will impose strict limitations on Facebook’s ability to collect and share data with third parties. And that decision appeared to help split the five-member commission. The 3-to-2 vote, taken in secret this week, drew the dissent of the two Democrats on the commission because they sought stricter limits on the company, the people said.",
        "quotes": [],
        "links": {
            "articles": [
                "https://www.nytimes.com/2019/04/24/technology/facebook-ftc-fine-privacy.html?module=inline"
            ],
            "gov_pgs": [],
            "unsure": []
        },
        "key_words": [
            "federal",
            "approves",
            "commission",
            "fine",
            "ftc",
            "vote",
            "facebook",
            "officials",
            "settlement",
            "trump",
            "technology",
            "billion",
            "powerful"
        ]
    },
    {
        "url": "https://www.bbc.co.uk/news/technology-45976300",
        "title": "Facebook fined £500,000 for Cambridge Analytica scandal",
        "authors": [],
        "publisher": "www.bbc.co.uk",
        "publish_date": "",
        "text": "Image copyright Getty Images Image caption Facebook's chief executive has repeatedly declined to answer questions from UK MPs about the scandal\n\nFacebook has been fined £500,000 by the UK's data protection watchdog for its role in the Cambridge Analytica data scandal.\n\nThe Information Commissioner's Office (ICO) said Facebook had let a \"serious breach\" of the law take place.\n\nThe fine is the maximum allowed under the old data protection rules that applied before GDPR took effect in May.\n\nThe ICO said Facebook had given app developers access to people's data \"without clear consent\".\n\nIn July, the ICO notified the social network that it intended to issue the maximum fine.\n\nConfirming the fine, it said in a statement: \"Between 2007 and 2014, Facebook processed the personal information of users unfairly by allowing application developers access to their information without sufficiently clear and informed consent, and allowing access even if users had not downloaded the app, but were simply 'friends' with people who had.\"\n\nMedia playback is unsupported on your device Media caption JULY 2018: Ms Denham warns Facebook\n\n\"Facebook also failed to keep the personal information secure because it failed to make suitable checks on apps and developers using its platform.\"\n\nFacebook said it was \"reviewing\" the ICO's decision.\n\n\"While we respectfully disagree with some of their findings, we have said before that we should have done more to investigate claims about Cambridge Analytica and taken action in 2015,\" it said in a statement.\n\nWhat was the Cambridge Analytica data scandal?\n\nResearcher Dr Aleksandr Kogan and his company GSR used a personality quiz to harvest the Facebook data of up to 87 million people.\n\nSome of this data was shared with Cambridge Analytica, which used it to target political advertising in the US.\n\n\"Even after the misuse of the data was discovered in December 2015, Facebook did not do enough to ensure those who continued to hold it had taken adequate and timely remedial action, including deletion,\" the ICO said.\n\nThe ICO found that more than one million people in the UK had their data harvested by the personality quiz.\n\n\"A company of its size and expertise should have known better and it should have done better,\" said Information Commissioner Elizabeth Denham.\n\nThe ICO is still investigating how data analytics is used for political purposes.\n\nMs Denham is due to give evidence to the Department for Digital, Culture, Media and Sport (DCMS) Select Committee on 6 November.",
        "quotes": [
            [
                "Between 2007 and 2014, Facebook processed the personal information of users unfairly by allowing application developers access to their information without sufficiently clear and informed consent, and allowing access even if users had not downloaded the app, but were simply 'friends' with people who had.",
                "",
                true
            ],
            [
                "Facebook also failed to keep the personal information secure because it failed to make suitable checks on apps and developers using its platform.",
                "Denham",
                true
            ],
            [
                "While we respectfully disagree with some of their findings, we have said before that we should have done more to investigate claims about Cambridge Analytica and taken action in 2015,",
                "",
                true
            ],
            [
                "Even after the misuse of the data was discovered in December 2015, Facebook did not do enough to ensure those who continued to hold it had taken adequate and timely remedial action, including deletion,",
                "",
                true
            ],
            [
                "A company of its size and expertise should have known better and it should have done better,",
                "Elizabeth Denham",
                true
            ]
        ],
        "links": {
            "articles": [
                "https://www.bbc.co.uk/news/av/technology-44006602/what-is-gdpr-technology-explained"
            ],
            "gov_pgs": [],
            "unsure": []
        },
        "key_words": [
            "500000",
            "data",
            "access",
            "scandal",
            "ico",
            "facebook",
            "information",
            "users",
            "analytica",
            "developers",
            "used",
            "cambridge",
            "fined"
        ]
    },
    {
        "url": "https://www.nytimes.com/2019/04/24/technology/facebook-ftc-fine-privacy.html?module=inline",
        "title": "Facebook Expects to Be Fined Up to $5 Billion by F.T.C. Over Privacy Issues",
        "authors": [
            {
                "name": "Cecilia Kang",
                "link": null
            },
            {
                "name": "Mike Isaac",
                "link": null
            }
        ],
        "publisher": "www.nytimes.com",
        "publish_date": "2019-04-24",
        "text": "SAN FRANCISCO — Facebook said on Wednesday that it expected to be fined up to $5 billion by the Federal Trade Commission for privacy violations. The penalty would be a record by the agency against a technology company and a sign that the United States was willing to punish big tech companies.\n\nThe social network disclosed the amount in its quarterly financial results, saying it estimated a one-time charge of $3 billion to $5 billion in connection with an “ongoing inquiry” by the F.T.C. Facebook added that “the matter remains unresolved, and there can be no assurance as to the timing or the terms of any final outcome.”\n\nFacebook has been in negotiations with the regulator for months over a financial penalty for claims that the company violated a 2011 privacy consent decree. That year, the social network promised a series of measures to protect its users’ privacy after an investigation found that its handling of data had harmed consumers.\n\nThe F.T.C. opened a new investigation last year after Facebook came under fire again. This time, the company was accused of not protecting its users’ data from being harvested without their consent by Cambridge Analytica, a British political consulting firm that was building voter profiles for the Trump campaign. Facebook also suffered a data breach that exposed the personal information of nearly 50 million users.",
        "quotes": [
            [
                "the matter remains unresolved, and there can be no assurance as to the timing or the terms of any final outcome.",
                "",
                false
            ]
        ],
        "links": {
            "articles": [
                "https://investor.fb.com/investor-news/press-release-details/2019/Facebook-Reports-First-Quarter-2019-Results/default.aspx",
                "https://www.nytimes.com/2018/03/17/us/politics/cambridge-analytica-trump-campaign.html?module=inline",
                "https://www.nytimes.com/2018/09/28/technology/facebook-hack-data-breach.html?module=inline",
                "https://www.nytimes.com/2019/02/14/technology/facebook-ftc-settlement.html?module=inline"
            ],
            "gov_pgs": [],
            "unsure": []
        },
        "key_words": [
            "expects",
            "data",
            "social",
            "privacy",
            "ftc",
            "penalty",
            "facebook",
            "network",
            "company",
            "users",
            "issues",
            "investigation",
            "billion",
            "fined"
        ]
    },
    {
        "url": "https://www.bbc.co.uk/news/av/technology-44006602/what-is-gdpr-technology-explained",
        "title": "What is GDPR? Technology explained",
        "authors": [],
        "publisher": "www.bbc.co.uk",
        "publish_date": "",
        "text": "Video\n\nA new EU law that changes how companies use our personal information kicks in on 25 May.\n\nThe BBC's Chris Foxx explains what GDPR is and how it will affect you.",
        "quotes": [],
        "links": {
            "articles": [],
            "gov_pgs": [],
            "unsure": []
        },
        "key_words": [
            "explains",
            "personal",
            "maythe",
            "kicks",
            "information",
            "law",
            "technology",
            "eu",
            "explained",
            "foxx",
            "videoa",
            "gdpr"
        ]
    }
]
```


