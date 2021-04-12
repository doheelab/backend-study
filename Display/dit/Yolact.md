## One stage detector

Classification, Localization를 동시에 수행

## 실시간 instance segmentation


- FCN을 사용하여 instance에 의존하지 않은 image 크기의 prototype masks 생성

- prototype 공간에서 instance의 정보를 가진 mask coefficients를 예측

or

- spatially coherent에 탁월한 conv layer을 통해 prototype masks를 생성

- semantic한 결과를 얻을 수 있는 fc layer을 통해 mask coefficients를 예측
  


![image](https://raw.githubusercontent.com/byeongjokim/byeongjokim.github.io/master/assets/images/YOLACT/architecture.PNG)

