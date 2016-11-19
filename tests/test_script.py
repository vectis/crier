import unittest
from crier.script import Script


class TestScript(unittest.TestCase):
    def test_normal_operation(self):
        headers = {'foo': 'bar'}
        response = {'baz': 'qux'}
        s = Script(123, headers=headers,
                   response=response, repeat=1)

        expected_response = (response, 123, headers)
        self.assertFalse(s.is_done)
        self.assertEqual(expected_response, s.next_response())

        self.assertFalse(s.is_done)
        self.assertEqual(expected_response, s.next_response())

        self.assertTrue(s.is_done)
        with self.assertRaises(RuntimeError):
            s.next_response()

    def test_defaults(self):
        s = Script(123)

        expected_response = ({}, 123, {})

        self.assertFalse(s.is_done)
        self.assertEqual(expected_response, s.next_response())
        self.assertTrue(s.is_done)

    def test_repeat_forever(self):
        s = Script(123, repeat=-1)

        expected_response = ({}, 123, {})

        self.assertFalse(s.is_done)
        self.assertEqual(expected_response, s.next_response())
        self.assertFalse(s.is_done)