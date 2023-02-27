At the bottom of this email you will find a OneTimeSecret link that, when clicked, contains credentials for a test committee in NGP 7. This key is unique to you, and it is essentially a password; please treat it with the same care that you would your own passwords and don't share it or post it online. If we find that you did, we will revoke it. Similarly, please don’t share this problem online, although it’s fine to ask questions on StackOverflow or elsewhere, provided you don’t share the API credentials or the text of the problem.

This problem is not intended to take more than an hour or two of work to complete; if you find yourself spending significantly more time than that, it’s worth rereading the requirements to see if you are overcomplicating things somewhere.

You will find the public API docs for NGP 7 here: https://docs.ngpvan.com/reference/getting-started-with-your-api-1 . It includes instructions and examples for connecting to, authenticating with, and consuming the NGP 7 API. For this problem, you will be using the /v2/BroadcastEmails endpoints, so you should pay particular attention to that section and to the main page on authentication.

If you have questions about the API or run into problems using it, you should email your hiring/recruiting contact for help, rather than going through the developer support portal. Please also feel free to reach out with any questions you have about the problem itself.


The Problem 

You work for an organization that sends emails to its supporters using NGP 7. You’ve been asked to produce a repeatable report of emails sent through the system, in order to track their performance.

The report should be formatted as a delimited file returned by your program. It should include all emails sent, in reverse order of sending based on EmailMessageId. For each email, you should display the EmailMessageID and name of the email, plus all available top-line stats (Recipients, Opens, Clicks, Unsubscribes, Bounces). Finally, you should include the name of the variant associated with that email that has the highest percentage-based performance on Opens.

Using the language and framework of your choice, write a script or program that produces the report described.

Example output (You do not need to match this exact format, so long as your output is as described above.):

>python take_home_problem.py

> Email report complete, file is EmailReport.csv

>cat EmailReport.csv

Email Message ID, Email Name, Recipients, Opens, Clicks, Unsubscribes, Bounces, Top Variant
2325647 "Join Us for a Howling Good Time!", 1599, 106, 27, 6, 4, "Don't Miss Our Grey Wolf Social"
2324747 "Get Your Gray Wolf Tote Bag: Donate Now!", 3541, 688, 147, 10, 8, "Furry Friends in Need"
2324646,"Tell Congress: Protect Gray Wolves", 2552, 343, 98, 5, 4, "Majestic Predators Need YOU"


Deliverables


Send us the following:

Your code for this project

Your answers to the follow-up questions

A .zip file, GitHub repo or gist, or Google Drive links are all acceptable ways to return your code; if none of those options work, please reach out and we’ll figure something else out.

Note: if you submit your code via a method that will make it publicly available, such as a public GitHub repo, please redact the API key before posting it; if we run your code we will provide our own key.

We may try to run your code, so it should be in as clean & working a state as possible, but we'll evaluate it whether it runs or not. If you’re unable to complete the problem, describe a solution using pseudocode.

We will evaluate your code on the following criteria:

Correctness. The logic should fulfill the requirements.

Clarity. Your solution should be straightforward.

Performance. Your solution should be as efficient as is reasonable while still prioritizing 1 and 2.


Follow-up Questions 
How long, roughly, did you spend working on this project? This won’t affect your evaluation; it helps us norm our problems to our expected time to complete them.

Give the steps needed to deploy and run your code, written so that someone else can follow and execute them.

What could you do to improve your code for this project if you had more time? Could you make it more efficient, easier to read, more maintainable? If it were your job to run this report monthly using your code, could it be made easier or more flexible? Give specifics where possible.

Outline a testing plan for this report, imagining that you are handing it off to someone else to test. What did you do to test this as you developed it? What kinds of automated testing could be helpful here?

Evaluation Criteria 
We will evaluate your code according to the following criteria, in order:

Correctness. The logic should fulfill the requirements.

Clarity. Your solution should be straightforward.

Performance. Your solution should be as efficient as is reasonable while still prioritizing 1 and 2.

We will evaluate your answers to the follow-up questions both for their technical proficiency and as an assessment of your written communication skills.