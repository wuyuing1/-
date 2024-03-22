import re

def get_province(id_num):
    province_dict = {
        '11': '京市', '12': '津市', '13': '冀省', '14': '晋省',
        '15': '内蒙古区', '21': '辽省', '22': '吉省', '23': '黑省',
        '31': '沪市', '32': '苏省', '33': '浙省', '34': '皖省', 
        '35': '闽省', '36': '赣省', '37': '鲁省', '41': '豫省', '42': '鄂省',
        '43': '湘省', '44': '粤省', '45': '桂区', '46': '琼省', '50': '渝市',
        '51': '川省', '52': '黔省', '53': '滇省', '54': '藏区', '61': '陕省',
        '62': '甘省', '63': '青省', '64': '宁区', '65': '新区', '71': '台省', 
        '81': '港区', '82': '澳区' } 
    province_code = id_num[:2]
    return province_dict.get(province_code, '未知')

def calculate_verify_code(id_num): 
    id_sum = sum(int(id_num[i]) * (2 ** (17 - i)) for i in range(17)) 
    verify_code = str((12 - id_sum % 11) % 11) 
    if verify_code == '10': 
        verify_code = 'X' 
    return verify_code

def check_id_card(id_num): 
    pattern = re.compile( r'^(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9Xx])$' )
    match = pattern.match(id_num)

    if match:
        area = get_province(id_num)
        day = f"{match.group(2)}-{match.group(3)}-{match.group(4)}"
        gender_code = match.group(5)
        gender = "男" if int(gender_code) % 2 == 1 else "女"
        verify_code = calculate_verify_code(id_num)
    
        if verify_code == match.group(6).upper():
            return f"所属地区：{area}，出生日期：{day}，性别：{gender}，检验数：{verify_code}，校验通过"
        else:
            return "校验失败：身份证号码校验码错误"
    else:
        return "输入的身份证号码格式不正确"
id_num = input("请输入您的身份证号码：") 
result = check_id_card(id_num) 
print(result)