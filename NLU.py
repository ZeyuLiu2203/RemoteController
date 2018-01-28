from __future__ import print_function
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, SemanticRolesOptions, ConceptsOptions, RelationsOptions


def extractKeywords(text):
	natural_language_understanding = NaturalLanguageUnderstandingV1(
		version='2017-02-27',
		username='9c5529fb-5b12-4248-ad9f-170c8ffc157d',
		password='yPpTRo31LHjW')

	response = natural_language_understanding.analyze(text=text,
		features=Features(
			keywords=KeywordsOptions(), semantic_roles=SemanticRolesOptions()))

	print(json.dumps(response, indent=2))	


extractKeywords('I would like to download the video congratulations')

