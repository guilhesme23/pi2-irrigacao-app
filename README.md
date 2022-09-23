# Grupo - Veículo autônomo de irrigação - PI2 - 2022/1

# Index

# Software

## App

### Backend

[Mapeamento](/backend/mapping/core/networkx_grid_route.py)

[Rota bot (Registrar/Ler Start/Stop)](/backend/api/src/routers/bot.py)

[Rota fields (Registrar/Ler campo)](/backend/api/src/routers/fields.py)

[Rota reports (Registrar/Ler status)](/backend/api/src/routers/reports.py)

[Rota sensors (Registrar/Ler dados dos sensores)](/backend/api/src/routers/sensors.py)

[Rota trajectory (Gerar/Ler rota com base no campo registrado)](/backend/api/src/routers/trajectory.py)

[Rota waterbalance (Ler Balanço hidrico)](/backend/api/src/routers/waterbalance.py)

[Banco de dados](/backend/api/src/database.py)

[Banco de dados de teste](/backend/tests/test_database.py)

[Models do Banco de dados](/backend/api/src/models.py)

[Manipulação do banco de dados (Registrar/Ler campo)](/backend/api/src/repositories/fields.py)

[Manipulação do banco de dados (Registrar/Ler Start/Stop)](/backend/api/src/repositories/irrigation.py)

[Manipulação do banco de dados (Registrar/Ler status)](/backend/api/src/repositories/reports.py)

[Manipulação do banco de dados (Registrar/Ler dados dos sensores)](/backend/api/src/repositories/sensors.py)

[Manipulação do banco de dados (Registrar/Ler rota)](/backend/api/src/repositories/trajectory.py)

[Testes do sofware de mapeamento](/backend/tests/mapping_test.py)

[Testes das rotas](/backend/tests/routes_test.py)

[Testes da manipulação do banco de dados](/backend/tests/repositories_test.py)

## Embarcados (eletroeletrônica)

[Rotina completa em Arduino](/embarcado/inttochar/inttochar.ino)

[Inicialização automática da rotina de irrigação, recepção de dados](/embarcado/Pegar_coordenadas.py)

[Automação de recepção e envio de métricas ambientais](/embarcado/receberDadosarduino.py)

[Execução manual de rotina de irrigação](/embarcado/exe_PI2.py)

[Testes de liga/desliga motobomba](/embarcado/irrigacao.py)

[Testes de movimentação](/embarcado/motor_PWM.py)

[Testes do IMU](/embarcado/mpu6050_filter.py)

[Teste do sonar como medição de distância](/embarcado/sensor_distancia.py)
