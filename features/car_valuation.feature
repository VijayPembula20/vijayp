Feature: Car Valuation

  Scenario Outline: Validate car details using registration number
    Given I navigate to the car valuation website
    When I search for a car with registration with "<registration>"
    And I enter the car "<mileage>"
    Then the car details should match the expected output
    Examples:
      | registration | mileage |
      | AD58 VNF     | 33000   |
      | BW57 BOW     | 24000   |

    Scenario: Validate car valuations against expected ouput
      Given I have an input file name "car_input.txt"
      When I extract vehicle registration numbers
      And I fetch valuations from the car valuation website
      Then I compare the fetched valuations with "car_output.txt"
      And I should see all mismatches highlighted


