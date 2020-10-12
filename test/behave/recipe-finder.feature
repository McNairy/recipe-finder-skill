Feature: Find recipes in an Elasticsearch database

  Scenario: Request recipe reply-with-dialog
    Given an English speaking user
    When the user says "find recipe berry"
    Then "recipe-finder" should reply with dialog from "recipe.finder.dialog"

  Scenario: Request recipe reply
    Given an English speaking user
    When the user says "find recipe berry"
    Then "recipe-finder" should reply with "Mixed Berry Shortcake"
