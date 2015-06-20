import sys
import unittest
from modules.engine import Engine
from tests.helpers import BaseTest

prompt = ">"

class EngineTest(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.fake_input, self.fake_print)

    def test_engine_enters_main_loop(self):
        try:
            self.say("Q")
            self.engine.main_loop()
        except AttributeError:
            self.fail("Engine does not have a main_loop() method")

    def test_engine_will_prompt_and_exit_with_q(self):
        self.say("Q")
        self.engine.main_loop()
        self.assertIn(prompt, ">")
        self.assertPrinted(prompt, 0)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e0a63b3... Adds main game loop and test helpers
=======
>>>>>>> 7dc09d9b4c73aa5e5294425bf2eead0caed827dc

    def test_engine_commands_are_not_case_sensitive(self):
        self.say("q")
        self.engine.main_loop()
        self.assertIn(prompt, ">")
        self.assertPrinted(prompt, 0)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 376ef97... Creates main loop and allows 'Q' to exit the main loop
=======
>>>>>>> e0a63b3... Adds main game loop and test helpers
=======
=======
>>>>>>> 5f1f848... Adds help menu
=======
>>>>>>> 7dc09d9b4c73aa5e5294425bf2eead0caed827dc

    def test_help_will_be_printed_when_asked_for(self):
        self.say("help")
        self.say("q")
        self.engine.main_loop()
        self.assertPrinted("help", 1)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4647ec3... Adds help menu
=======
>>>>>>> 5f1f848... Adds help menu
=======
>>>>>>> 7dc09d9b4c73aa5e5294425bf2eead0caed827dc