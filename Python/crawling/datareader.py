# 출처: https://wendys.tistory.com/174?category=769564 [웬디의 기묘한 이야기]

import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt

# 종목 타입에 따라 download url이 다름. 종목코드 뒤에 .KS .KQ등이 입력되어야해서 Download Link 구분 필요
stock_type = {
'kospi': 'stockMkt',
'kosdaq': 'kosdaqMkt'
}
# 회사명으로 주식 종목 코드를 획득할 수 있도록 하는 함수
def get_code(df, name):
  code = df.query("name=='{}'".format(name))['code'].to_string(index=False)
  # 위와같이 code명을 가져오면 앞에 공백이 붙어있는 상황이 발생하여 앞뒤로 sript() 하여 공백 제거
  code = code.strip()
  return code
# download url 조합
def get_download_stock(market_type=None):
  market_type = stock_type[market_type]
  download_link = 'http://kind.krx.co.kr/corpgeneral/corpList.do'
  download_link = download_link + '?method=download'
  download_link = download_link + '&marketType=' + market_type
  df = pd.read_html(download_link, header=0)[0]
  return df;
# kospi 종목코드 목록 다운로드
def get_download_kospi():
  df = get_download_stock('kospi')
  df.종목코드 = df.종목코드.map('{:06d}.KS'.format)
  return df
# kosdaq 종목코드 목록 다운로드
def get_download_kosdaq():
  df = get_download_stock('kosdaq')
  df.종목코드 = df.종목코드.map('{:06d}.KQ'.format)
  return df
# kospi, kosdaq 종목코드 각각 다운로드
kospi_df = get_download_kospi()
kosdaq_df = get_download_kosdaq()
# data frame merge
code_df = pd.concat([kospi_df, kosdaq_df])
# data frame정리
code_df = code_df[['회사명', '종목코드']]
# data frame title 변경 '회사명' = name, 종목코드 = 'code'
code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})
# 삼성전자의 종목코드 획득. data frame에는 이미 XXXXXX.KX 형태로 조합이 되어있음
code = get_code(code_df, '삼성전자')
# get_data_yahoo API를 통해서 yahho finance의 주식 종목 데이터를 가져온다.
df = pdr.get_data_yahoo(code)



# 단순이동평균
df['sma2'] = df['Close'].rolling(2).mean()
df['sma5'] = df['Close'].rolling(5).mean()
df['sma20'] = df['Close'].rolling(20).mean()
df['sma100'] = df['Close'].rolling(100).mean()
df['sma200'] = df['Close'].rolling(200).mean()


# 지수 이동평균 EMA: 보다 최근의 값에 가중치
df['ema5'] = df['Close'].ewm(5).mean()
df['ema20'] = df['Close'].ewm(20).mean()
df['ema100'] = df['Close'].ewm(100).mean()
df['ema200'] = df['Close'].ewm(200).mean()

df_plot = df['2019-01-01'<= df.index]


# 현재 data frame에서 Close(종가) 기준으로 그래프를 생성
plt.plot(figsize=(6,6))
plt.plot(df_plot['Close'], label="close")
plt.plot(df_plot['sma20'], label="sma20")
plt.plot(df_plot['ema20'], label="ema20")
plt.legend()
plt.show()
