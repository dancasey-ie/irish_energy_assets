import unittest
import app


class TestApp(unittest.TestCase):
    def test_list_attr_values(self):
        """
        Tests function returns sorted list of all possible values of a defined attiribute in
        all docs in defined collection. All values must be of same type.
        """
        collection = [{"Index": 1, "Attribute1": 11,
                       "Attribute2": "Ethan", "Attribute3": "4"},
                      {"Index": 2, "Attribute1": 12,
                       "Attribute2": "Dave", "Attribute3": "9"},
                      {"Index": 3, "Attribute1": 13,
                       "Attribute2": "charlie"},
                      {"Index": 4, "Attribute1": 14,
                       "Attribute2": "Beth"},
                      {"Index": 5, "Attribute1": 15,
                       "Attribute2": "adam", "Attribute3": "6"}]

        self.assertEqual(app.list_attr_values("Index", collection),
                         [1, 2, 3, 4, 5])
        self.assertEqual(app.list_attr_values("Attribute1", collection),
                         [11, 12, 13, 14, 15])
        self.assertEqual(app.list_attr_values("Attribute2", collection),
                         ["adam", "beth", "charlie", "dave", "ethan"])
        self.assertEqual(app.list_attr_values("Attribute3", collection),
                         ["4", "6", "9"])

    def test_list_attr_collection(self):
        """
        Tests function returns sorted list of all attributes in all docs in defined
        collection. Attributes are case sensitive.
        """
        collection = [{"Index": 1, "Attribute1": 11,
                       "Attribute2": "Ethan", "Attribute3": "4"},
                      {"Index": 2, "Attribute1": 12,
                       "Attribute2": "Dave", "attribute3": "9"},
                      {"Index": 3, "Attribute1": 13,
                       "Attribute2": "charlie"},
                      {"Index": 4, "Attribute1": 14,
                       "Attribute2": "Beth"},
                      {"Index": 5, "Attribute1": 15,
                       "Attribute2": "adam", "Attr3": "6"}]
        self.assertEqual(app.list_attr_collection(collection),
                         ["Attr3", "Attribute1", "Attribute2",
                          "Attribute3", "Index", "attribute3"])

    def test_list_attr_dict(self):
        """
        Tests function returns sorted list of dictionaries, each dictionary correspounds to a
        attribute value in collection. Dictionary contains attribute value,
        number of docs with attribute value in collection and sum of MEC_MW
        attribute for docs with attribute value.
        """
        collection = [{"Index": 1, "Attribute1": "11",
                       "Attribute2": "Ethan", "Attribute3": "4"},
                      {"Index": 2, "Attribute1": 12.666886,
                       "Attribute2": "Charlie", "attribute3": "9"},
                      {"Index": 3, "Attribute1": 13.001122112,
                       "Attribute2": "beth"},
                      {"Index": 4, "Attribute1": 14,
                       "Attribute2": "ethan"},
                      {"Index": 5,
                       "Attribute2": "adam", "Attr3": "6"}]
        self.assertEqual(app.list_attr_dict("Index", "Attribute1",
                                            collection),
                         [{'Name': 1, 'Count': 1, 'Total': 11.00},
                          {'Name': 2, 'Count': 1, 'Total': 12.67},
                          {'Name': 3, 'Count': 1, 'Total': 13.00},
                          {'Name': 4, 'Count': 1, 'Total': 14.00}])
        self.assertEqual(app.list_attr_dict("Attribute2", "Attribute1",
                                            collection),
                         [{'Name': "Beth", 'Count': 1, 'Total': 13.00},
                          {'Name': "Charlie", 'Count': 1, 'Total': 12.67},
                          {'Name': "Ethan", 'Count': 2, 'Total': 25.00}])

    def test_sort_collection(self):
        """
        Tests function sorts a collection based on attribute.
        Case sensitive.
        """
        collection = [{"Index": 1, "Attribute1": "11",
                       "Attribute2": "Ethan", "Attribute3": "4"},
                      {"Index": 2, "Attribute1": 12.666886,
                       "Attribute2": "Charlie", "attribute3": "9"},
                      {"Index": 3, "Attribute1": 13.001122112,
                       "Attribute2": "beth"},
                      {"Index": 4, "Attribute1": 14,
                       "Attribute2": "ethan"},
                      {"Index": 5,
                       "Attribute2": "adam", "Attr3": "6"}]
        self.assertEqual(app.sort_collection("Index", False, collection),
                         collection)
        self.assertEqual(app.sort_collection("Index", True, collection),
                         [{"Index": 5,
                           "Attribute2": "adam", "Attr3": "6"},
                          {"Index": 4, "Attribute1": 14,
                           "Attribute2": "ethan"},
                          {"Index": 3, "Attribute1": 13.001122112,
                           "Attribute2": "beth"},
                          {"Index": 2, "Attribute1": 12.666886,
                           "Attribute2": "Charlie", "attribute3": "9"},
                          {"Index": 1, "Attribute1": "11",
                           "Attribute2": "Ethan", "Attribute3": "4"}])
        self.assertEqual(app.sort_collection("Attribute2", False, collection),
                         [{"Index": 2, "Attribute1": 12.666886,
                           "Attribute2": "Charlie", "attribute3": "9"},
                          {"Index": 1, "Attribute1": "11",
                           "Attribute2": "Ethan", "Attribute3": "4"},
                          {"Index": 5,
                           "Attribute2": "adam", "Attr3": "6"},
                          {"Index": 3, "Attribute1": 13.001122112,
                           "Attribute2": "beth"},
                          {"Index": 4, "Attribute1": 14,
                           "Attribute2": "ethan"}])

    def test_get_total(self):
        """
        Tests function returns sum of values of defined attribute in defined collection.
        """
        collection = [{"Index": 1, "Attribute1": "11",
                       "Attribute2": "Ethan", "Attribute3": "4"},
                      {"Index": 2, "Attribute1": 12.666886,
                       "Attribute2": "Charlie", "attribute3": "9"},
                      {"Index": 3, "Attribute1": 13.001122112,
                       "Attribute2": "beth"},
                      {"Index": 4, "Attribute1": 14,
                       "Attribute2": "ethan"},
                      {"Index": 5,
                       "Attribute2": "adam", "Attr3": "6"}]
        self.assertEqual(app.get_total("Index", collection), 15)
        self.assertEqual(app.get_total("Attribute1", collection), 50.67)

    def test_search_collection(self):
        """
        Tests collection filter for keyword.
        Returns subset of defined collection that contains the defined
        keyword in its attribute values.
        """
        collection = [{"Index": 1, "Attribute1": "11",
                       "Attribute2": "Ethan", "Attribute3": "4"},
                      {"Index": 2, "Attribute1": 12.666886,
                       "Attribute2": "Charlie", "attribute3": "9"},
                      {"Index": 3, "Attribute1": 13.001122112,
                       "Attribute2": "beth"},
                      {"Index": 4, "Attribute1": 14,
                       "Attribute2": "ethan"},
                      {"Index": 5,
                       "Attribute2": "adam", "Attr3": "6"}]
        self.assertEqual(app.search_collection("Ethan", collection),
                         [{"Index": 1, "Attribute1": "11",
                           "Attribute2": "Ethan", "Attribute3": "4"},
                          {"Index": 4, "Attribute1": 14,
                           "Attribute2": "ethan"}])
        self.assertEqual(app.search_collection("1", collection),
                         [{"Index": 1, "Attribute1": "11",
                           "Attribute2": "Ethan", "Attribute3": "4"},
                          {"Index": 2, "Attribute1": 12.666886,
                           "Attribute2": "Charlie", "attribute3": "9"},
                          {"Index": 3, "Attribute1": 13.001122112,
                           "Attribute2": "beth"},
                          {"Index": 4, "Attribute1": 14,
                           "Attribute2": "ethan"}])
        self.assertEqual(app.search_collection("Index", collection), [])

    def test_filter_collection(self):
        """
        Tests sollection filter for attribute list of values.
        Returns subset of collection that defined attribute's value is in
        defined list of values.

        """
        collection = [{"Index": 1, "Attribute1": "11",
                       "Attribute2": "Ethan", "Attribute3": "4"},
                      {"Index": 2, "Attribute1": 12.666886,
                       "Attribute2": "Charlie", "attribute3": "9"},
                      {"Index": 3, "Attribute1": 13.001122112,
                       "Attribute2": "beth"},
                      {"Index": 4, "Attribute1": 14,
                       "Attribute2": "ethan"},
                      {"Index": 5,
                       "Attribute2": "adam", "Attr3": "6"}]
        self.assertEqual(app.filter_collection("Attribute2", ["Adam"],
                                               collection),
                         [{"Index": 5, "Attribute2": "adam", "Attr3": "6"}])
        self.assertEqual(app.filter_collection("Attribute2",
                                               ["Adam", "ethan"],
                                               collection),
                         [{"Index": 1, "Attribute1": "11",
                           "Attribute2": "Ethan", "Attribute3": "4"},
                          {"Index": 4, "Attribute1": 14,
                           "Attribute2": "ethan"},
                          {"Index": 5, "Attribute2": "adam", "Attr3": "6"}])
        self.assertEqual(app.filter_collection("Attribute2", [""],
                                               collection), [])
        self.assertEqual(app.filter_collection("Attr3", [6, 10], collection),
                         [{"Attr3": "6", "Attribute2": "adam", "Index": 5}])

    def test_filter_attr_range(self):
        """
        Tests collection filter for attribute value within range.
        Returns subset of collection that defined attribute's value is between
        defined range set by hi and lo constraints.
        """
        collection = [{"Index": 1, "Attribute1": "11",
                       "Attribute2": "Ethan", "Attribute3": "4"},
                      {"Index": 2, "Attribute1": 12.666886,
                       "Attribute2": "Charlie", "attribute3": "9"},
                      {"Index": 3, "Attribute1": 13.001122112,
                       "Attribute2": "beth"},
                      {"Index": 4, "Attribute1": 14,
                       "Attribute2": "ethan"},
                      {"Index": 5,
                       "Attribute2": "adam", "Attr3": "6"}]
        self.assertNotEqual(app.filter_attr_range("Attribute1", 12.67, 13.5,
                                                  collection),
                            [{"Attribute1": 12.666886,
                              "Attribute2": "Charlie",
                              "attribute3": "9", "Index": 2},
                             {"Attribute1": 13.001122112,
                              "Attribute2": "beth", "Index": 3}])
        self.assertEqual(app.filter_attr_range("Attribute1", 12.66, 13.5,
                                               collection),
                         [{"Attribute1": 12.666886,
                           "Attribute2": "Charlie",
                           "attribute3": "9", "Index": 2},
                          {"Attribute1": 13.001122112,
                           "Attribute2": "beth", "Index": 3}])
        self.assertNotEqual(app.filter_attr_range("Attribute1", 12.66, 13,
                                                  collection),
                            [{"Attribute1": 12.666886,
                              "Attribute2": "Charlie",
                              "attribute3": "9", "Index": 2},
                             {"Attribute1": 13.001122112,
                              "Attribute2": "beth", "Index": 3}])
        self.assertEqual(app.filter_attr_range("Attribute1", 12.66, 13.0012,
                                               collection),
                         [{"Attribute1": 12.666886,
                           "Attribute2": "Charlie",
                           "attribute3": "9", "Index": 2},
                         {"Attribute1": 13.001122112,
                          "Attribute2": "beth", "Index": 3}])
