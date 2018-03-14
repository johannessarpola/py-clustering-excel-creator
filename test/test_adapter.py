import unittest
from context import adapter, relative_resource_json


class ModelTest(unittest.TestCase):
    def test_clustering_result(self):
        json = relative_resource_json('example_result.json')
        mr = adapter.multiple_results_from_json(json)

        actIds = ['TFIDF_Combined',
                  'TFIDF_Keywords',
                  'TFIDF_KeywordsFirst',
                  'TFIDF_WordNgram',
                  'WikipediaTitles']

        ids = list(map(lambda cr: cr.id, mr))
        cls = list(map(lambda cr: cr.clusters, mr))

        self.assertSequenceEqual(actIds, ids)

        for c in cls:
            self.assertEqual(9, len(c))