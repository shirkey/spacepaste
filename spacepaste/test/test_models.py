import unittest

from spacepaste import application, models
from spacepaste.database import db

class ModelsTest(unittest.TestCase):
    def setUp(self):
        self.app = application.make_app("sqlite://", "secret")
        self.private_parent = models.Paste("", "text", None, None, True)
        db.session.add(self.private_parent)
        db.session.commit()

    def add_private(self, parent=None):
        paste = models.Paste("", "text", parent, None, True)
        db.session.add(paste)
        db.session.commit()
        return paste

    def test_private_reply(self):
        # XXX Ideally, there should be some timeout or something
        self.add_private(self.private_parent)

    def test_private_pastes_not_in_find_all(self):
        pastes = list(models.Paste.find_all())
        self.assertEqual(pastes, [])

    def test_get_wrong_identifier(self):
        paste = self.add_private(self.private_parent)
        self.assertEqual(models.Paste.get(paste.paste_id), None)

    def test_resolve_root_private_no_parent(self):
        root = models.Paste.resolve_root(self.private_parent.identifier)
        self.assertEqual(root.identifier, self.private_parent.identifier)


if __name__ == "__main__":
    unittest.main()
