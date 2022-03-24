from flask_wtf import FlaskForm #Biblioteca criação formulario
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from paginaunicasite.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField('Nome do Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Cadastrar')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. cadastre um novo e-mail ou faça login para continuar')


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Senha de Acesso')
    botao_submit_login = SubmitField('Entrar')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome do Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto Perfil', validators=[FileAllowed(['jpg', 'png'])])
    curso_excel = BooleanField('Excel Avançado')
    curso_powerbi = BooleanField('Power BI Avançado')
    curso_sql = BooleanField('SQL Avançado')
    curso_python = BooleanField('Python Avançado')
    curso_vba = BooleanField('VBA Avançado')
    curso_ppt = BooleanField('PPT Avançado')
    botao_submit_editarperfil = SubmitField('Alterar E-Mail')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com esse e-mail. Cadastre um novo e-mail')


class FormCriarPost(FlaskForm):
    titulo = StringField('Titulo do post', validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Escreva o seu post aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')