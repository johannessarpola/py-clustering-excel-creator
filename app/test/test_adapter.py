import unittest
from app.test.context import relative_resource_json
from app.src import adapter


class ModelTest(unittest.TestCase):
    def test_clustering_result(self):
        json = relative_resource_json('example_result.json')
        mr = adapter.multiple_results_from_json([json])[0] # only single file

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

    def test_cluster_categories(self):
        json = relative_resource_json('example_result.json')
        mr = adapter.multiple_results_from_json([json])[0] # only single file

        all_clusters = list(map(lambda cr: cr.clusters, mr))
        ids = set()
        cats = set()
        for cs in all_clusters:
            for c in cs:
                ids.add(c.id)
                for k in c.categories.keys():
                    cats.add(k)
                self.assertIsNotNone(c.id)
                self.assertIsNotNone(c.categories)

        self.assertEqual(9, len(ids))
        self.assertEqual(3, len(cats))
