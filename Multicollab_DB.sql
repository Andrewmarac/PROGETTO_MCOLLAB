drop table Influencer

CREATE TABLE Influencer(
    Screen_Name varchar(50) not null,
    Name_ varchar(50) not null,
    Number_of_Followers int,
    Location_ varchar(50),
    Category_ varchar(50)
	primary key(Screen_Name)
    foreign key(Category_) references Category(Nome)
);

select * from Influencer

select * from Azienda