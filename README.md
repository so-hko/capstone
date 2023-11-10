# Meditory : 이미지 인식 기반 의약정보 제공 시스템
project for capstone, computer science of Kyonggi University <br>
## 0. 시스템 구상도 

  ## 1. 개발 필요성 및 목적
 본 프로젝트를 수행하게 된 배경은 팬데믹 현상으로 인한 다양한 약품에 대한 수요와 관심이 늘어남에 있다. 정확한 의학 정보를 얻으려는 소비자들의 요구에 따라 제약업계들이 개선된 정보전달을 위해 발 빠르게 움직이고 있다. 최근에는 의약품의 포장 개선에 대한 필요성이 이슈화되고 있는데, 관련이 없는 약품임에도 불구하고 비슷한 겉포장 탓에 처방 과정에서나 사용자가 약품을 복용하는 과정에서 실수가 발생하기 때문이다. 심지어 상반된 약품임에도 겉포장이 유사하여 제대로 구분하지 못해 오남용하는 치명적인 문제가 빈번하게 일어난다고 한다. 또한 가정에서 알 수 없이 흩어진 알약들이나 모르는 언어의 약품들을 발견했을 때, 해외에서 급하게 의약품이 필요할 때 등등, 일상생활에서도 의약정보 제공 어플리케이션의 필요성을 쉽게 느낄 수 있다. 
 기존의 유사 프로그램들은 사용자가 직접 정보를 검색창에 입력하여 의약품 정보를 얻는 방법이 대부분이다. 약품 포장지에 적혀있는 언어가 외국어이거나 사용자가 알아볼 수 없는 경우에는 검색과 정보전달의 과정이 원만하게 이루어질 수 없다. 그러므로 사용자의 직접적인 입력 없이도 사진 촬영만으로 약품을 인식하는 기능이 탑재된 애플리케이션의 개발을 통해서 불편함을 개선하려 한다. 물론, 보통 의약품 검색 프로그램들이 제공하는 주 기능인 의약품의 모양, 색깔, 식별자를 기입하여 검색하는 기능도 존재하지만 본 프로그램은 검색 후 정보를 사용자가 설정한 언어로 번역해준다는 점에서 차별성을 보인다. 즉, 사용자는 애플리케이션을 통해 언제 어디서나 쉽게 필요한 의약품의 정보를 원하는 언어로 받을 수 있고, 더불어 제약제품 및 의학 정보에 대한 수요를 만족시킬 수 있다.


## 2. 주요 기술 접근 방법

 ### 2-1. GOOGLE VISION API를 이용한 이미지 내 텍스트 디텍션
 본 프로젝트에서는 Google Vision API와 GOOGLE Translate API를 사용하여 이미지 탐지와 번역을 위한 자연어 처리를 진행한다. Google Vision API는 사용자가 이미지를 파일 형식으로 업로드하고 나면 이미지 속에서 블록 형태로 라벨을 할당한다. 라벨 할당 후 OCR 기술을 사용하여 라벨 속의 텍스트를 인식하고 데이터를 수집한다. 수집된 데이터를 분석하고 통계 처리가 가능한 형태로 변환시키는 자연어 처리 과정을 거쳐 사용자에게 읽어낸 텍스트를 전송한다.
<br>● OCR : 
 GOOGLE VISION API의 주요 기술은 기계로 인쇄되거나 사람이 직접 쓴 문자를 기계가 읽을 수 있는 문자로 변환하는 광학 문자 인식인 OCR 기술이다. 문서 속 문자만 인식했던 기술과는 달리 Google에서 제공하는 API로 사진이나 영상 속 문자까지 인식하는 성능을 보여준다. 또한, 컴퓨터가 직접 대량의 데이터를 학습함으로써 이미지에서 텍스트를 인식하는 규칙을 만들어낸다. 딥러닝을 기반으로 둔 OCR 기술은 이미지의 전처리 과정을 통해 컴퓨터가 쉽게 인식할 수 있도록 보정 하는 과정을 거친다. 그 후 텍스트 디텍션을 통해 딥러닝 시스템을 이용하여 전체 이미지에서 텍스트인 영역을 골라내는 작업을 수행한다. 이미지에서 문자 영역을 추출하고 난 후에는 다량의 데이터로 학습을 통해 그 문자가 어떤 문자를 나타내는지 알아낸다. 마지막으로는 텍스트 부분에서 상황에 맞는 후처리 과정을 거친다. <br>
 ### 2-2. GOOGLE TRANSLATE API를 이용한 약 정보 번역
  Google Translate API는 텍스트 마이닝을 통해 저장된 데이터를 각 클라이언트의 국가 언어로 번역하기 위해 구글에서 제공하는 Translate API를 사용하였다. Google Translate API는 용어 또는 구문을 분야 및 문맥에 맞춰 판단하고 데이터의 언어를 자동으로 구별하여 제공한다. 선행 학습된 머신러닝 모델로 여러 가지 언어를 신속하게 동적으로 번역할 수 있다. 
 ### 2-3. 텍스트 유사도 분석
 <p align='center'><img src=https://user-images.githubusercontent.com/64884935/223363142-8fb3d77a-6a91-4c68-bf19-106d93bafe64.png ></p>

 ## 3. 캡스톤디자인 연구내용
### 4-1. 프로젝트 역할분담
#### 4-1-1. 프로젝트 역할분담
