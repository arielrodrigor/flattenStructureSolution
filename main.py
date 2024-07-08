import copy
import unittest

def flatten_structure(data):
    if isinstance(data, dict):
        new_data = {}
        for key, value in data.items():
            if isinstance(value, list):
                singular_key = key[:-1] if key.endswith('s') else None
                new_data[key] = [flatten_structure(item[singular_key]) if singular_key and isinstance(item, dict) and singular_key in item else flatten_structure(item) for item in value]
            else:
                new_data[key] = flatten_structure(value)
        return new_data
    elif isinstance(data, list):
        return [flatten_structure(item) for item in data]
    else:
        return data

# Usage
data = {
    "attribute_one": "foo",
    "posts": [
        {"post": {"name": "p1", "content": "post one"}},
        {"post": {"name": "p2", "content": "post two"}},
        {"post": {"name": "p3", "content": "post three"}}
    ]
}

flattened_data = flatten_structure(data)
print(flattened_data)

# Test cases
class TestFlattenStructure(unittest.TestCase):

    def test_flatten_structure_simple(self):
        data = {
            "attribute_one": "foo",
            "posts": [
                {"post": {"name": "p1", "content": "post one"}},
                {"post": {"name": "p2", "content": "post two"}},
                {"post": {"name": "p3", "content": "post three"}}
            ]
        }
        expected = {
            "attribute_one": "foo",
            "posts": [
                {"name": "p1", "content": "post one"},
                {"name": "p2", "content": "post two"},
                {"name": "p3", "content": "post three"}
            ]
        }
        self.assertEqual(flatten_structure(data), expected)

    def test_flatten_structure_nested(self):
        data = {
            "attribute_one": "foo",
            "details": {
                "comments": [
                    {"comment": {"user": "u1", "message": "message one"}},
                    {"comment": {"user": "u2", "message": "message two"}}
                ]
            }
        }
        expected = {
            "attribute_one": "foo",
            "details": {
                "comments": [
                    {"user": "u1", "message": "message one"},
                    {"user": "u2", "message": "message two"}
                ]
            }
        }
        self.assertEqual(flatten_structure(data), expected)

    def test_flatten_structure_no_change(self):
        data = {
            "attribute_one": "foo",
            "details": {
                "comments": [
                    {"user": "u1", "message": "message one"},
                    {"user": "u2", "message": "message two"}
                ]
            }
        }
        expected = copy.deepcopy(data)
        self.assertEqual(flatten_structure(data), expected)

    def test_flatten_structure_mixed(self):
        data = {
            "users": [
                {"user": {"id": 1, "name": "Alice"}},
                {"user": {"id": 2, "name": "Bob"}}
            ],
            "comments": [
                {"comment": {"id": 1, "text": "Nice post!"}},
                {"comment": {"id": 2, "text": "Thanks for sharing."}}
            ]
        }
        expected = {
            "users": [
                {"id": 1, "name": "Alice"},
                {"id": 2, "name": "Bob"}
            ],
            "comments": [
                {"id": 1, "text": "Nice post!"},
                {"id": 2, "text": "Thanks for sharing."}
            ]
        }
        self.assertEqual(flatten_structure(data), expected)

    def test_flatten_structure_multiple_levels(self):
        data = {
            "level_one": {
                "level_two": {
                    "items": [
                        {"item": {"id": 1, "value": "A"}},
                        {"item": {"id": 2, "value": "B"}}
                    ]
                }
            }
        }
        expected = {
            "level_one": {
                "level_two": {
                    "items": [
                        {"id": 1, "value": "A"},
                        {"id": 2, "value": "B"}
                    ]
                }
            }
        }
        self.assertEqual(flatten_structure(data), expected)

    def test_flatten_structure_with_non_standard_keys(self):
        data = {
            "data_points": [
                {"data_point": {"x": 1, "y": 2}},
                {"data_point": {"x": 3, "y": 4}}
            ],
            "measurements": [
                {"measurement": {"temp": 20, "humidity": 30}},
                {"measurement": {"temp": 22, "humidity": 35}}
            ]
        }
        expected = {
            "data_points": [
                {"x": 1, "y": 2},
                {"x": 3, "y": 4}
            ],
            "measurements": [
                {"temp": 20, "humidity": 30},
                {"temp": 22, "humidity": 35}
            ]
        }
        self.assertEqual(flatten_structure(data), expected)

if __name__ == '__main__':
    unittest.main()
