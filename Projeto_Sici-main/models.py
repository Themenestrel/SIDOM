# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Dados(models.Model):
    cd_ua = models.IntegerField(blank=True, null=True)
    sigla_ua = models.CharField(max_length=100, blank=True, null=True)
    nome_ua = models.CharField(max_length=255, blank=True, null=True)
    titular = models.CharField(max_length=255, blank=True, null=True)
    cargo = models.CharField(max_length=255, blank=True, null=True)
    cd_ua_pai = models.IntegerField(blank=True, null=True)
    cd_ua_basica = models.IntegerField(blank=True, null=True)
    nome_ua_basica = models.CharField(max_length=255, blank=True, null=True)
    sigla_ua_basica = models.CharField(max_length=255, blank=True, null=True)
    nat_juridica = models.IntegerField(blank=True, null=True)
    ordem_ua_basica = models.IntegerField(blank=True, null=True)
    ordem_absoluta = models.IntegerField(blank=True, null=True)
    ordem_relativa = models.IntegerField(blank=True, null=True)
    tipo_logradouro = models.CharField(max_length=255, blank=True, null=True)
    nome_logradouro = models.CharField(max_length=500, blank=True, null=True)
    trechamento_cep = models.CharField(db_column='trechamento_CEP', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nome_logradouro_abreviado = models.CharField(max_length=500, blank=True, null=True)
    nro = models.IntegerField(blank=True, null=True)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    bairro_abreviado = models.CharField(max_length=255, blank=True, null=True)
    localidade = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(db_column='CEP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telefones = models.CharField(max_length=1000, blank=True, null=True)
    emails = models.CharField(max_length=1000, blank=True, null=True)
    horario_funcionamento = models.CharField(max_length=255, blank=True, null=True)
    msg = models.TextField(blank=True, null=True)  # This field type is a guess.
    data_criacao_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dados'


class Diario(models.Model):
    id_integer = models.AutoField(db_column='ID_Integer', primary_key=True)  # Field name made lowercase.
    diariodata = models.DateField(db_column='DiarioData', blank=True, null=True)  # Field name made lowercase.
    data = models.TextField(db_column='Data', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    numprocesso = models.TextField(db_column='NumProcesso', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    numcto = models.TextField(db_column='NumCto', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    anocto = models.TextField(db_column='AnoCto', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ug = models.TextField(db_column='UG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    partes = models.TextField(db_column='Partes', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    objeto = models.TextField(db_column='Objeto', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    valor = models.TextField(db_column='Valor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pt = models.TextField(db_column='PT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fundamento = models.TextField(db_column='Fundamento', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ptnumeros = models.TextField(db_column='PTNumeros', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    anoctoug = models.TextField(db_column='AnoCtoUG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    numctovisualizacao = models.TextField(db_column='NumCtoVisualizacao', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    anoctovisualizacao = models.TextField(db_column='AnoCtoVisualizacao', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ptnumvisualizacao = models.TextField(db_column='PTNumVisualizacao', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    deletar = models.TextField(db_column='Deletar', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    especie = models.TextField(db_column='Especie', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    observacoes = models.TextField(db_column='Observacoes', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Diario'


class MdContratosDiario(models.Model):
    data_diario = models.DateField()
    data_assinatura = models.CharField(max_length=200, blank=True, null=True)
    num_contrato = models.CharField(max_length=200, blank=True, null=True)
    ano_contrato = models.CharField(max_length=200, blank=True, null=True)
    ug_contrato = models.CharField(max_length=20, blank=True, null=True)
    valor_contrato = models.CharField(max_length=20, blank=True, null=True)
    ano_visualizacao = models.CharField(max_length=200, blank=True, null=True)
    deletar = models.CharField(max_length=20, blank=True, null=True)
    especie = models.CharField(max_length=20, blank=True, null=True)
    fundamento = models.CharField(max_length=500, blank=True, null=True)
    num_cto_visualizacao = models.CharField(max_length=200, blank=True, null=True)
    num_processo = models.CharField(max_length=400, blank=True, null=True)
    objeto = models.CharField(max_length=1000, blank=True, null=True)
    observacoes = models.CharField(max_length=1000, blank=True, null=True)
    partes = models.CharField(max_length=500, blank=True, null=True)
    pt = models.CharField(max_length=500, blank=True, null=True)
    pt_numeros = models.CharField(max_length=50, blank=True, null=True)
    pt_visualizacao = models.CharField(max_length=50, blank=True, null=True)
    anoctoug = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MD_contratos_diario'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
