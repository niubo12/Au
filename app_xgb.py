import streamlit as st
import pandas as pd
import joblib

# 配置 Streamlit 页面
st.set_page_config(
    page_title="Au-Leaching Prediction",
    page_icon="🔬"
)
 
# 直接显示欢迎信息（无需登录）
st.write('Welcome Au leaching prediction!')
 
# 加载模型（无需等待登录）
xgb_Au = joblib.load('xgb_Au.pkl')

 
st.title('Predict Au-Leaching')
 
dict1 = {
    'X12': {
        "H2SO4": 98,
        "Ammonium hydroxide": 35
    },
    'X14': {
        "Thiourea": 76.1,
        "(NH4)2S2O3": 148,
        "NaCl": 58.5,
        "NaBr": 103,
        "Na2S2O3": 158,
        "KI": 166
    },
    'X16': {
        "Fe2(SO4)3": 400,
        "FeCl3·6H2O": 270.5,
        "I2": 254,
        "Na2S2O8": 238,
        "CuSO4": 159.6    
    } 
}
       
   

X1 = st.sidebar.slider(label = 'Particle size(um)', min_value = 75.0,
                              max_value = 3000.0 ,
                              value = 500.0,
                              step = 20.0)
                               
X2 = st.sidebar.slider(label = 'Cu in Feed(wt%)', min_value = 0.104,
                              max_value = 97.24 ,
                              value = 0.20,
                              step = 0.01)    
X3 = st.sidebar.slider(label = 'Al in Feed(wt%)', min_value = 0.0,
                              max_value =34.1 ,
                              value = 0.28,
                              step = 0.0001) 
X4 = st.sidebar.slider(label = 'Fe in Feed(wt%)', min_value = 0.0,
                              max_value = 15.12 ,
                              value = 0.014,
                              step = 0.0001)
X5 = st.sidebar.slider(label = 'Ni in Feed(wt%)', min_value = 0.094,
                              max_value = 6.04 ,
                              value = 4.83,
                              step = 0.5) 
X6 = st.sidebar.slider(label = 'Pb in Feed(wt%)', min_value = 0.03,
                              max_value = 6.7 ,
                              value = 1.27,
                              step = 1.0) 
X7 = st.sidebar.slider(label = 'Zn in Feed(wt%)', min_value = 0.0,
                              max_value = 2.23 ,
                              value = 0.92,
                              step = 0.1) 
X8 = st.sidebar.slider(label = 'Au in Feed(wt%)', min_value = 0.0043,
                              max_value = 0.64,
                              value = 0.52,
                              step = 0.1) 
X9 = st.sidebar.slider(label = 'Ag in Feed(wt%)', min_value = 0.02,
                              max_value = 0.82,
                              value = 0.75,
                              step = 0.1)                         
X10 = st.sidebar.slider(label = 'Sn in Feed(wt%)', min_value = 0.159,
                              max_value = 9.2,
                              value = 3.06,
                              step = 0.1)                         
X11 = st.sidebar.slider(label = 'Pd in Feed(wt%)', min_value = 0.007,
                              max_value = 0.039,
                              value = 0.0045,
                              step = 0.1)                          
                         
   
X12 = st.sidebar.selectbox('Leaching agent1', ["H2SO4",
"Ammonium hydroxide"
])                         
    
    
X13 = st.sidebar.slider(label = '1-Conc(M) ', min_value = 0.01,
                              max_value = 3.0,
                              value = 0.0,
                              step = 0.1)
X14 = st.sidebar.selectbox('Leaching agent2', ["Thiourea",
        "(NH4)2S2O3",
        "NaCl",
        "NaBr",
        "Na2S2O3",
        "KI"
]) 

X15 = st.sidebar.slider(label = '2-Conc(g/L) ', min_value = 0.761,
                              max_value = 309.0,
                              value = 100.0,
                              step = 10.0)
                              
X16 = st.sidebar.selectbox('Leaching agent3', ["Fe2(SO4)3",
        "FeCl3·6H2O",
        "CuSO4",
        "Na2S2O8",        
        "I2"                         
])                             
X17 = st.sidebar.slider(label = '3-Conc(g/L)  ', min_value = 0.0,
                              max_value = 29.9,
                              value = 1.0,
                              step = 0.5)

X18 = st.sidebar.slider(label = 'H2O2(M)', min_value = 0.0,
                              max_value = 3.92,
                              value = 1.0,
                              step = 0.5)
       
X19 = st.sidebar.slider(label = 'Time(min) ', min_value = 0.0,
                              max_value = 2880.0,
                              value = 150.0,
                              step = 10.0)    
X20 = st.sidebar.slider(label = 'Temperature(℃) ', min_value = 20.0,
                              max_value = 90.0,
                              value = 55.0,
                              step = 1.0)    
X21 = st.sidebar.slider(label = 'Pulp density(g/L) ', min_value = 2.85,
                              max_value = 200.0,
                              value = 150.0,
                              step = 0.1)    
X22 = st.sidebar.slider(label = 'Stirring speed(rpm)', min_value = 100.0,
                              max_value = 700.0,
                              value = 150.0,
                              step = 10.0)    
        
features = {'Particle size':X1, 'Cu in Feed':X2, 'Al in Feed':X3, 'Fe in Feed':X4, 'Ni in Feed':X5,
       'Pb in Feed':X6, 'Zn in Feed':X7, 'Au in Feed':X8, 'Ag in Feed':X9, 'Sn in Feed':X10, 'Pd in Feed':X11,  
        'Leaching agent1':dict1['X12'][X12], 
       '1-Conc ':X13, 'Leaching agent2':dict1['X14'][X14], '2-Conc ':X15, 'Leaching agent3':dict1['X16'][X16], '3-Conc  ':X17, 'H2O2':X18,
        'Time ':X19, 'Temperature ':X20, 'Pulp density ':X21, 'Stirring speed':X22,
      }
features_df  = pd.DataFrame([features])
st.dataframe(
    features_df,
    use_container_width=True,  # 自动适应容器宽度
    height=100  # 可选：固定高度触发垂直滚动
) 

# 预测按钮逻辑（保持不变）
if st.button('Predict'):
    # Au-Leaching 预测
    prediction_Au = xgb_Au.predict(features_df)
    au_leaching = max(0, min(100, prediction_Au[0]))
    st.write(f' Au-Leaching: {au_leaching:.1f}%')  # 修正点
 
   

                          
    
