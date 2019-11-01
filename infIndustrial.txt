### Preâmbulo
drop database deizanos;

### Criacação do banco de dados
create database deizanos;
use deizanos;

create table localizacao (
	idLocalizacao int auto_increment,
    nomeLocalizacao varchar(50) NOT NULL,
    rua varchar(50),
    bairro varchar(50),
    cidade varchar(50),
    PRIMARY KEY(idLocalizacao)
);

create table equipamento (
	idEquipamento int auto_increment,
    nomeEquipamento varchar(50) NOT NULL,
    tipo enum('Lâmpada', 'Ventilador'),
    estado boolean,
    idLocalizacaoFK int,
    PRIMARY KEY (idEquipamento),
    FOREIGN KEY (idLocalizacaoFK) REFERENCES localizacao(idLocalizacao)
);

create table usuario (
	idUsuario int auto_increment,
    nomeUsuario varchar(50) NOT NULL,
    nomeTratamento varchar(50),
    idLocalizacaoFK int,
    PRIMARY KEY (idUsuario),
    FOREIGN KEY (idLocalizacaoFK) REFERENCES localizacao(idLocalizacao)
);

create table comando (
	idComando int auto_increment,
    acao varchar(50) NOT NULL,
    idUsuarioFK int,
    PRIMARY KEY (idComando),
    FOREIGN KEY (idUsuarioFK) REFERENCES usuario(idUsuario)
);

create table anotacao (
	idAnotacao int auto_increment,
	dataCriacao DATETIME NOT NULL,
    conteudo varchar(100),
    idUsuarioFK int,
    PRIMARY KEY (idAnotacao),
    FOREIGN KEY (idUsuarioFK) REFERENCES usuario(idUsuario)
);

/*
describe localizacao;
describe equipamento;
describe usuario;
describe comando;
describe anotacao;
*/

### Populando o banco de dados
insert into localizacao
(nomeLocalizacao, rua, bairro, cidade)
values
('Casa de Porto', 'Marechal', 'Prata', 'Campina Grande');

insert into localizacao
(nomeLocalizacao, rua, bairro, cidade)
values
('Casa de Luska', 'Antônio Alves', 'Princesinha', 'Pau dos Ferros');

insert into equipamento
(nomeEquipamento, estado, tipo, idLocalizacaoFK)
values
('Luz do quarto', 0, 'Lâmpada', 1);

insert into equipamento
(nomeEquipamento, estado, tipo, idLocalizacaoFK)
values
('Luz do sala', 0, 'Lâmpada', 1);

insert into equipamento
(nomeEquipamento, estado, tipo, idLocalizacaoFK)
values
('Ventilador do quarto', 0, 'Ventilador', 1);

insert into equipamento
(nomeEquipamento, estado, tipo, idLocalizacaoFK)
values
('Luz da cozinha', 0, 'Lâmpada', 2);

insert into usuario
(nomeUsuario, nomeTratamento, idLocalizacaoFK)
values
('Lucas Porto', 'Portoo', 1);

insert into usuario
(nomeUsuario, nomeTratamento, idLocalizacaoFK)
values
('Lucas Figueiredo', 'Luquinha', 2);

insert into comando
(acao, idUsuarioFK)
values
('Ligar luz do quarto', 1);

insert into comando
(acao, idUsuarioFK)
values
('Ligar luz da sala', 1);

insert into comando
(acao, idUsuarioFK)
values
('Ligar luz da cozinha', 2);

insert into anotacao
(dataCriacao, conteudo, idUsuarioFK)
values
(CURRENT_DATE(), 'Dentista segunda às 16h', 1);

insert into anotacao
(dataCriacao, conteudo, idUsuarioFK)
values
(CURRENT_DATE(), 'Comprar pilhas para a HP', 1);

insert into anotacao
(dataCriacao, conteudo, idUsuarioFK)
values
(CURRENT_DATE(), 'Smirnoff em promoção no Hiper!', 2);

### Consultas

# Quais equipamentos estão localizados em Campina Grande?
select * 
from equipamento inner join localizacao on equipamento.idLocalizacaoFK = localizacao.idLocalizacao
where cidade = 'Campina Grande';

# Quantas anotações o usuário X (escolher um usuário) tem?
select count(*)
from anotacao
where idUsuarioFK = 1;

# Quais os comandos o usuário X fez?
select *
from comando
where idUsuarioFK = 1;