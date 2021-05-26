drop table Influencer

CREATE TABLE Influencer(
    Screen_Name varchar(50) not null,
    Name_ varchar(50) ,
    Number_of_Followers int,
    Location_ varchar(50),
    Category_ varchar(50),
    Url_ varchar(100),
    Description varchar(500),
    Profile_image VARCHAR(200),
	primary key(Screen_Name),
    foreign key(Category_) references Category(Nome)
);


select * from Influencer
drop table Azienda
CREATE Table Azienda(
        nome varchar(50) not null,
        localita varchar(50) not null,
        slogan varchar(50) not null,
        Primary key (nome)    
)
Insert into Azienda values('Ciripasta','Milano', 'Let The Good Times Roll.')
Insert into Azienda values('ALLORA EH','Roma','life loves you')
Insert into Azienda values('Pasta e pizza',' Bergamo','I Wish They All Could Be Good Girls.')
Insert into Azienda values('CDVINTAGE','Trieste','Nothing Sucks Like A Good.')
Insert into Azienda values('FITSPORT','Milano','Sport Is Going Places')
Insert into Azienda values('SAVELIFE','Milano','The Real Smell Of Sport.')
Insert into Azienda values('Culture','Milano','Dont Worry, Art Takes Care.')
Insert into Azienda values('LiveThePast','Roma','Challenge Art.')
Insert into Azienda values('PCLOCK','Milano','Are You Ready For Tech?')
Insert into Azienda values('SIUUUUUUUM','Milano','Cristiano Ronaldo, Couldnt Be Better!')
Insert into Azienda values('RICH&POOR','Milano','Fashion Will Get You More Girls.')
Insert into Azienda values('SHIIIC','Bergamo','Fashion For A Professional Image.')
Insert into Azienda values('CHEEESE','Milano','LOOOOOK AT HIM')
Insert into Azienda values('Marasigan store','Milano','im the best')
Insert into Azienda values('LEESSGOO','Milano','Oh My Goddess, It s A Lees Go.')
Insert into Azienda values('LEGOLEGOLAND','MIlano','Look For The Lego Label')
Insert into Azienda values('JORDAN','Milano','Michael Jordan was here')
Insert into Azienda values('FOOTBALL CLUB','Milano','Better than MESSI+Ronaldo')
Insert into Azienda values('MR PC','Milano','treat well your pc and stay safe')
Insert into Azienda values('TECHEDGE','Milano','My Techedge And Me.')
Insert into Azienda values('ART SALON','Milano','Beaty is the perfection')
Insert into Azienda values('LOL','Milano','I cant smile')
Insert into Azienda values('NERDSLETSGO','Milano','WE ARE NERDS ')
Insert into Azienda values('PastaEater','Milano','Pasta lover')
Insert into Azienda values('Drink%JOKE','Milano','Have fun with the best drinks')
Insert into Azienda values('SEXY MUSCLES','Milano','Try to touch it')
Insert into Azienda values('We love together','Milano','Learn how to date')
Insert into Azienda values('Teach Tech','Milano','PRO PRO PRO PRO PRO')
Insert into Azienda values('Believe me','Milano','I believe i can fly')
Insert into Azienda values('TTTTTTTT','Milano','TROLL and have fun')
Insert into Azienda values('BRBRBRBR','Milano','Sound like an animal')
select * from Azienda
