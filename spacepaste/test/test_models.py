import unittest

from spacepaste import application, models
from spacepaste.database import db

class ModelsTest(unittest.TestCase):
    def setUp(self):
        self.app = application.make_app("sqlite://", "secret")
        self.private_parent = models.Paste("", "text", None, None, True)
        db.session.add(self.private_parent)
        db.session.commit()

    def test_private_reply(self):
        # XXX Ideally, there should be some timeout or something
        paste = models.Paste("", "text", self.private_parent, None, True)
        db.session.add(paste)
        db.session.commit()

if __name__ == "__main__":
    unittest.main()
