INSERT INTO user (firstname, lastname, about, phone, email) 
VALUES 
    ('John', 'Doe', 'Some information about John', '+1234567890', 'john@example.com'),
    ('Alice', 'Smith', 'Some information about Alice', '+9876543210', 'alice@example.com'),
    ('Bob', 'Johnson', 'Some information about Bob', '+1112223333', 'bob@example.com'),
    ('Emily', 'Brown', 'Some information about Emily', '+4445556666', 'emily@example.com'),
    ('Michael', 'Wilson', 'Some information about Michael', '+7778889999', 'michael@example.com'),
    ('Emma', 'Jones', 'Some information about Emma', '+2223334444', 'emma@example.com'),
    ('William', 'Taylor', 'Some information about William', '+6667778888', 'william@example.com'),
    ('Olivia', 'Anderson', 'Some information about Olivia', '+9990001111', 'olivia@example.com'),
    ('James', 'Martinez', 'Some information about James', '+3334445555', 'james@example.com'),
    ('Sophia', 'Garcia', 'Some information about Sophia', '+8889990000', 'sophia@example.com');


INSERT INTO Skill (name, description, user_id)
VALUES ('Python', 'Programming language', 2),
       ('JavaScript', 'Web development language', 2),
       ('HTML', 'Markup language for web development', 3),
       ('CSS', 'Styling language for web development', 4),
       ('Java', 'General-purpose programming language', 5),
       ('SQL', 'Structured Query Language', 6),
       ('C++', 'General-purpose programming language', 7),
       ('React', 'JavaScript library for building UI', 8),
       ('Angular', 'Web application framework', 9),
       ('Django', 'Web framework for Python', 10);
       
       
       INSERT INTO project (name, image, description, user_id) VALUES
('Project 1', 'image1.jpg', 'Description 1', 1),
('Project 2', 'image2.jpg', 'Description 2', 1),
('Project 3', 'image3.jpg', 'Description 3', 2),
('Project 4', 'image4.jpg', 'Description 4', 12),
('Project 5', 'image5.jpg', 'Description 5', 3),
('Project 6', 'image6.jpg', 'Description 6', 7),
('Project 7', 'image7.jpg', 'Description 7', 9),
('Project 8', 'image8.jpg', 'Description 8', 10),
('Project 9', 'image9.jpg', 'Description 9', 6),
('Project 10', 'image10.jpg', 'Description 10', 5);

INSERT INTO education (organization, description, start_at, end_at, user_id) VALUES
('University 1', 'Degree in Computer Science', '2020-09-01', '2024-06-30', 1),
('College 1', 'Diploma in Electrical Engineering', '2018-08-01', '2020-05-30', 1),
('School 1', 'High School Diploma', '2014-09-01', '2018-06-30', 1),
('University 2', 'Masters in Business Administration', '2019-09-01', '2021-06-30', 2),
('College 2', 'Diploma in Mechanical Engineering', '2017-08-01', '2019-05-30', 2),
('School 2', 'High School Diploma', '2013-09-01', '2017-06-30', 2),
('University 3', 'Degree in Psychology', '2018-09-01', '2022-06-30', 3),
('College 3', 'Diploma in Civil Engineering', '2016-08-01', '2018-05-30', 3),
('School 3', 'High School Diploma', '2012-09-01', '2016-06-30', 3),
('University 4', 'PhD in Physics', '2021-09-01', '2025-06-30', 4);



INSERT INTO Social (name, url, user_id) VALUES
('Facebook', 'https://www.facebook.com/user1', 1),
('Twitter', 'https://twitter.com/user2', 2),
('Instagram', 'https://www.instagram.com/user3', 3),
('LinkedIn', 'https://www.linkedin.com/in/user4', 4),
('GitHub', 'https://github.com/user5', 5),
('Facebook', 'https://www.facebook.com/user6', 6),
('Twitter', 'https://twitter.com/user7', 7),
('Instagram', 'https://www.instagram.com/user8', 8),
('LinkedIn', 'https://www.linkedin.com/in/user9', 9),
('GitHub', 'https://github.com/user10', 10);


-- Insert values into the job_type table
INSERT INTO job_type (name) VALUES
('Software Engineer'),
('Data Scientist'),
('Project Manager'),
('Business Analyst'),
('UI/UX Designer');

-- Insert values into the experience table
INSERT INTO experience (job, description, start_at, end_at, user_id, job_type_id) VALUES
('Software Developer', 'Developed web applications using Python and Django', '2020-01-01', '2021-06-30', 1, 1),
('Data Analyst', 'Analyzed large datasets to derive insights for business decisions', '2019-07-01', '2020-12-31', 2, 2),
('Project Manager', 'Managed cross-functional teams to deliver projects on time and within budget', '2018-03-01', '2019-12-31', 3, 3),
('Business Analyst', 'Conducted market research and prepared reports for strategic decision-making', '2017-01-01', '2018-02-28', 4, 4),
('UI/UX Designer', 'Designed user interfaces for mobile and web applications', '2016-04-01', '2016-12-31', 5, 5),
('Software Engineer', 'Developed scalable backend systems using Java and Spring', '2020-02-01', '2021-07-31', 6, 1),
('Data Scientist', 'Built machine learning models for predictive analytics', '2019-08-01', '2020-11-30', 7, 2),
('Project Manager', 'Led software development projects from initiation to delivery', '2018-04-01', '2019-11-30', 8, 3),
('Business Analyst', 'Performed data analysis to identify business opportunities', '2017-02-01', '2018-01-31', 9, 4),
('UI/UX Designer', 'Created wireframes and prototypes for mobile applications', '2016-05-01', '2017-01-31', 10, 5);


       
select * from education 