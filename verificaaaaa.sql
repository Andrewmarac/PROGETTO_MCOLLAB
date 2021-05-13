--Medico(CodiceM, Nome, cognome, specializzazione, città, telefono)
--Paziente(CodiceSSN, Nome, cognome, DataNascita, Città, telefono)
--Visita(CodiceMedico*, CodicePaziente*, Data, Diagnosi, CodiceMedicinale*)
--Medicinale(Codice, Nome, principioAttivo, Prezzo)


--Medico(CodiceM, Nome, cognome, specializzazione, città, telefono)
CREATE TABLE Medico(
	CodiceM varchar(50) not null,
	Nome varchar(50) not null,
	Cognome varchar(50) not null,
	Specializzazione varchar(50) not null,
	Citta varchar(50) not null,
	telefono int not null

	primary key(CodiceM)
);

insert into Medico values('bswe','Robertina','Trevisani','Malattie infettive','Milano',5346346)
insert into Medico values('biod','Angelo','Palermo','Cardiologia','Lecce',534563645)
insert into Medico values('budw','Antonio','Marino','Nefrologia','Roma',7756756)
insert into Medico values('bxxc','Chiarina','De Luca','Pediatria','Napoli',64564547)
insert into Medico values('brsf','Giosuè','Ferri','Medicina termale','Milano',7567567)

--Paziente(CodiceSSN, Nome, cognome, DataNascita, Città, telefono)
CREATE TABLE Paziente(
	CodiceSSN varchar(50) not null,
	Nome varchar(50) not null,
	Cognome varchar(50) not null,
	DataNascita DATE not null,
	Citta varchar(50) not null,
	Telefono int not null,

	primary key(CodiceSSN)
);

insert into Paziente values('aqsw','Terzo ','Donini','1999-04-13','Milano',3282160571)
insert into Paziente values('abmf','Nazario','Canali','1984-04-12','Roma',123124234)
insert into Paziente values('aogv','Berengar','Opizzi','2002-04-14','Bergmao',42352345)
insert into Paziente values('axvd','Alberto','Ferrari','1997-04-15','Torino',53453455)
insert into Paziente values('abge','Fonsie','Genovese','2005-04-16','Genova',867456455)

--Medicinale(Codice, Nome, principioAttivo, Prezzo)
CREATE TABLE Medicinale(
	Codice varchar(50) not null,
	Nome varchar(50) not null,
	PrincipioAttivo varchar(50) not null,
	Prezzo decimal(6,2) not null,

	primary key(Codice)
);
insert into Medicinale values('mgfs','Aliskiren','pa1',99)
insert into Medicinale values('mggf','Aulin','pa2',34.45)
insert into Medicinale values('mkk3','Apremilast','pa3',25.0)
insert into Medicinale values('msdg','Boceprevir','pa4',45.0)
insert into Medicinale values('mjk0','Bosutinib','pa5',10.00)
insert into Medicinale values('mkdgg','emicrania','pa6',20.00)


--Visita(CodiceMedico*, CodicePaziente*, Data, Diagnosi, CodiceMedicinale*)
CREATE TABLE Visita(
	CodiceMedico varchar(50) not null,
	CodicePaziente varchar(50) not null,
	Data_ date not null,
	Diagnosi varchar(50) not null,
	CodiceMedicinale varchar(50) not null,

	primary key(CodiceMedico,CodicePaziente,Data_),
	foreign key(CodiceMedico) references Medico(CodiceM),
	foreign key(CodicePaziente) references Paziente(CodiceSSN),

	foreign key(CodiceMedicinale) references Medicinale(Codice)
);

select * from Visita

insert into Visita values('bswe','abmf','2005-03-10','anemia','mggf')
insert into Visita values('biod','abmf','2005-06-12','anemia','mggf')
insert into Visita values('budw','aogv','2005-07-13','anemia','mggf')

insert into Visita values('bxxc','axvd','2010-08-14','epilessia','mjk0')
insert into Visita values('brsf','abge','2014-09-15','epilessia','mjk0')

insert into Visita values('bxxc','aogv','2011-08-14','emicrania','mggf')
insert into Visita values('brsf','axvd','2012-09-15','emicrania','mggf')


--QUERY
--Determinare nome e cognome dei pazienti, nati dopo il 1980, che assumono il medicinale ‘Aulin’ per curare l’emicrania
select pz.nome, pz.cognome
from Visita as vst
JOIN Paziente as pz on vst.CodicePaziente = pz.CodiceSSN
JOIN Medicinale as md on vst.CodiceMedico = md.Codice
Where year (pz.DataNascita) > '1980' and md.Nome = 'Aulin' and vst.Diagnosi = 'emicrania'


--Determinare il numero dei pazienti che nel 2005 hanno curato l’anemia
select count(*) as 'Numero paziente'
from Visita as vst
JOIN Paziente as pz on vst.CodicePaziente = pz.CodiceSSN
where year (vst.Data_) = '2005' and vst.Diagnosi = 'anemia'

--Determinare il numero dei pazienti che sono stati curati per ciascuna specializzazione prevista
select pz.Specializzazione, count(CodiceSSN) as 'Numero paziente'
from Visita as vst
JOIN Paziente as pz on vst.CodicePaziente = pz.CodiceSSN
GROUP BY pz.Specializzazione
--Calcolare la media dei prezzi spesi da ciascun paziente per l’acquisto dei medicinali per la diagnosi ‘epilessia’
--Dato il nome e il cognome del medico visualizzare la sua specializzazione e l’elenco dei pazienti che hanno prenotato una visita in una determinata data.
--Provare tutte le query e fornire i tabulati delle elaborazioni di tutte le operazione svolte.