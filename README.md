# README

# Support Vectory - Project 3

## Problem Statement

Is it possible to detect depression or anxiety in text "speech patterns?"

To this end we'd develop a NLP classification model that can seperate classes "depression" and "anxiety" from an input document.

## Executive Summary

To begin exploring this problem we model a simplified adjacent supervised learning problem: classify a document(post or submission) as originating from r/depression or r/Anxiety.

Throughout the modeling process evidence for the following hypothesis is explored:

Latent features present in text produce a signature, or idiosyncratic sense of voice, specific to the "depressed sense of voice" or the "anxious sense of voice." In extension:
* The depressed voice is interally focused and language tends toward self-reference.
* The anxious voice is externally focused and language tends toward the other.

Furthermore the problem is framed as proposal review within a made up company "Support Vector." This company is a mental health app that utilizes NLP/NLU to detect "signs before symptoms." The proposal is an exploration of additions to the company's language models(the above hypothesis).

To begin "we" scrape posts from r/depression and r/Anxiety using pushshift API.

EDA reveals a significant number of deleted, removed, and empty posts. Occasionally this is moderator intervention in most cases they are deleted by the user(particularly in r/depression ~ 12.5% of posts were null due to frequent deletion by user). Some seasonality in volume of posts to r/depression and r/Anxiety is evident, but a greater timespan would need to be sampled to confirm.

Preprocessing removes posts below 15 words and above 800 words to sculpt the corpus. We want the model to learn from word choice and exploring our hypothesis to learn from linguistic features/lexical items. We do not want the model to learn to classify posts based on word count. Tokenization, stopword removal, and sentiment analysis are performed at this stage. This is done to reduce dimensionality and remove low information terms from our corpus(e.g. My/my, a, it).

Classes are balanced to be 50-50. Models are trialed using accuracy, precision, and recall. Special attention is paid to precision as we are looking to minimize our type I error or false positive rate(FPR). The applicaiton of our model is to detect is medical and is meant to assist rather than replace a human element. We want to minimize telling a user that they are exhibiting features of depression or anxiety when they are not. This could trigger or exacerbate symptoms leading to a positive feedback loop contributing to a problem we are trying to mitigage.

Logistic regression scores highest on metrics of accuracy, precision, and related scores(AUC). Accuracy is recorded as 91.9%(train) 91.1%(test), precision as 89.7% with an AUC of 97%.

This model is deployed using Streamlit:

https://share.streamlit.io/mirage137/streamlit/Support_Vector.py

Within the code a confidence threshold is set as greater than 75% either class. Below that the app will return "do not know." This reframes the classes as can classify or can't classify, but reduces "false positives" on text input that does not satisfy the threshold.

Explanatory data analysis is attempted to look at frequent n-grams and compare them to our model's coefficients. Coefficients that explicitly mention depression and anxiety while power predictors of class obscure inferential and/or latent features in our data.

The model is a success in that we can classify a docuement as originating from r/depression or r/anxiety. As to the hypothesis and more general problem statement...
The strength of the model, mixed classes, and presence of strong positive and negative predictors being present in both classes suggests a fundametal error in reasoning and/or latent variables.

Next steps would include multiclass classification with a neutral reference point(source: r/AskReddit). Consultation with SMEs in Linguistics and factor analysis(Psychology)
Use embedding models, refined language models, and so called ”cheating” models presented in https://arxiv.org/pdf/2001.01941.pdf

This model is a relevant starting point and exploration in how to begin the detection of mental health issues by latent features. It is my personal proposal that one of the greatest potentials of "learning" is the detection of latent features at scales humans are incapable of. The human faculty of insight and intuition might often be dectection of latent features by blackbox models internal and near inacessible(at least obscured) to an individual's brain.