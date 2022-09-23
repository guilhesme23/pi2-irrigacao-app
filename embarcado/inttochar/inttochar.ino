#include <dht.h>
#include <VirtualWire.h>
//#include <VirtualWire_Config.h>
#include <stdio.h>

  // DEFINIR OS PINOS DE ENTRADA
const int pinoDHT11 = A2; //PINO ANALÓGICO UTILIZADO PELO DHT11
const int pinoSensorSolo = A1; //PINO UTILIZADO PELO SENSOR
  // DEFINIR PARÂMETROS DE LEITURA DO SENSOR RESISTIVO
const int analogSoloSeco = 1020; //VALOR MEDIDO COM O SOLO SECO (VOCÊ PODE FAZER TESTES E AJUSTAR ESTE VALOR)
const int analogSoloMolhado = 220; //VALOR MEDIDO COM O SOLO MOLHADO (VOCÊ PODE FAZER TESTES E AJUSTAR ESTE VALOR)
const int percSoloSeco = 0; //MENOR PERCENTUAL DO SOLO SECO (0% - NÃO ALTERAR)
const int percSoloMolhado = 100; //MAIOR PERCENTUAL DO SOLO MOLHADO (100% - NÃO ALTERAR)
  // VARIÁVEL DE ACORDO COM A BIBLIOTECA DHT
dht DHT;
  // VARIÁVEL PARA ARMAZENAR A LEITURA ANALÓGICA
int valorLidoSolo, valorLidoSolo2; //VARIÁVEL QUE ARMAZENA O PERCENTUAL DE UMIDADE DO SOLO
int umidadeAr, TempAr;
char inicio[5] = "0000";
char fim[5] = "1111";
char umidadeSolo[4];
char umidadeAr2[4];
char TempAr2[4];
String message;

void setup() {
  //INICIALIZAR PROTOCOLO SERIAL
   Serial.begin(9600);
   vw_set_tx_pin(2);
   vw_setup(2000);
}

void loop() {
      // LÊ O DHT PELA BIBLIOTECA
    DHT.read11(pinoDHT11);
      // LÊ O SENSOR RESISTIVO E ARMAZENA
    //valorLidoSolo = constrain(analogRead(pinoSensorSolo),analogSoloMolhado,analogSoloSeco); //TENTATIVA DE LIMITAR OS VALORES LIDOS
    valorLidoSolo = analogRead(pinoSensorSolo);
    int valorLidoSolo2 = map(valorLidoSolo,analogSoloSeco,analogSoloMolhado,percSoloSeco,percSoloMolhado); //EXECUTA A FUNÇÃO "map" DE ACORDO COM OS PARÂMETROS PASSADOS

    int umidadeAr = DHT.humidity;
    int TempAr = DHT.temperature;
    sprintf(umidadeSolo,"%3d", valorLidoSolo2);
    sprintf(umidadeAr2,"%3d", umidadeAr);
    sprintf(TempAr2,"%3d", TempAr);

    send(inicio);
    Serial.println("inicio");
    send(umidadeSolo);
    Serial.println(umidadeSolo);
    send(umidadeAr2);
    Serial.println(umidadeAr2);
    send(TempAr2);
    Serial.println(TempAr2);
    send(fim);
    Serial.println("fim");
      // ESCREVE O VALOR DA UMIDADE DO AR
    //Serial.print("Umidade do ar: ");
    //Serial.print(DHT.humidity);
    //Serial.println("%"); //ESCREVE O TEXTO EM SEGUIDA
      // ESCREVE O VALOR DA TEMPERATURA DO AR
   // Serial.print("Temperatura: ");
    //Serial.print(DHT.temperature, 0); // ZERO CASAS DECIMAIS
   // Serial.println("°C");
      // ESCREVE O VALOR DA UMIDADE DO SOLO   
    //Serial.print("Umidade do solo: "); 
    //Serial.print(valorLidoSolo2);
    //Serial.println("%");
      // DEFINE O TEMPO ENTRE AS LEITURAS EM MILISSEGUNDOS
    delay(30000);
}

  void send (char *message)
{
    vw_send((uint8_t *)message, strlen(message));
    vw_wait_tx(); // aguarda o envio de dados
}
