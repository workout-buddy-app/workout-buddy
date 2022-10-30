CREATE DATABASE IF NOT EXISTS motivational_quotes;

USE motivational_quotes;

CREATE TABLE inspirational_quotes(
				quotes VARCHAR(255) NOT NULL
);

INSERT INTO inspirational_quotes
(quotes)
VALUES
('Progress, Not Perfection.'),
('You can do ANYTHING for 2 minutes!'),
('It only takes one step to get started. – Andrea Metcalf'),
('Any movement is good movement. – Nicole Nichols'),
('The groundwork for all happiness is good health. – Leigh Hunt'),
('All great achievements require time. — Maya Angelou'),
('Dieting helps you look better in clothes; exercise helps you look better naked!'),
('Definition of a really good workout; when you hate doing it, but you love finishing it.'),
('Someone busier than you is working out right now.'),
('All our dreams can come true if we have the courage to pursue them. — Walt Disney'),
('The body achieves what the mind believes.'),
('Success usually comes to those who are too busy to be looking for it. — Henry David Thoreau'),
('Believe in yourself and all that you are.'),
('Obstacles can’t stop you. Problems can’t stop you. People can’t stop you. Only you can stop you.'),
('A one hour workout is 4% of your day. No Excuses!'),
('Your body can stand almost anything. It’s your mind that you have to convince.'),
('Work hard in silence. Let success be your noise.'),
('What hurts today makes you stronger tomorrow. — Jay Cutler'),
('Action is the foundational key to all success. — Pablo Picasso'),
('The only bad workout is the one that didn’t happen.'),
('You have to think it before you can do it. The mind is what makes it all possible. — Kai Greene'),
('If you still look good at the end of your workout, you didn’t train hard enough.'),
('It’s actually pretty simple. Either you do it, or you don’t.'),
('Don’t limit your challenges, challenge your limits.'),
('I am stronger today than I was yesterday.'),
('The pain you feel today, will be the strength you feel tomorrow.'),
('Good things come to those who sweat.'),
('The successful warrior is the average woman, with laser-like focus.'),
('The only place where success comes before work is in the dictionary. — Vidal Sassoon'),
('If something stands between you and your success, move it. Never be denied. — Dwayne ‘The Rock’ Johnson'),
('Motivation is what gets you started. Habit is what keeps you going.'),
('Well done is better than well said. — Benjamin Franklin'),
('There is no perfect body except the one you woke up in. Enjoy it! – Rachel Cosgrove'),
('All progress takes place outside the comfort zone. — Michael John Bobak'),
('Push yourself because no one else is going to do it for you.'),
('Making excuses burns zero calories per hour.'),
('Know that there is something inside of you that is greater than any obstacle.'),
('The hardest lift of all is lifting your bottom off the sofa.'),
('Never give up on a dream just because of the time it will take to accomplish it. The time will pass anyway.'),
('You must expect great things of yourself before you can do them. — Michael Jordan'),
('You are stronger than you think.'),
('When you feel like quitting, think about why you started.'),
('No matter how slow you go, you’re still lapping those on their sofa.'),
('Nothing truly great ever came from a comfort zone.'),
('What seems impossible today will one day become your warm-up.'),
('It’s not how you start; it’s how you finish. — Amy Dixon'),
('Commit to being the very best version of yourself today! — Lindsay Vastola'),
('And though she be but little, she is fierce. – William Shakespeare'),
('Don’t train to be skinny. Train to be a bad ass. – Demi Lovato'),
('There are seven days in a week. Someday is not one of them.'),
('It doesn’t get easier. You get stronger.')
;

SELECT * FROM inspirational_quotes;