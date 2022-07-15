# AiogramPagination

Аргументы класса InlinePagionation:  

1.button_datas просто данные в списке которые надо использовать в callback_data  в названиях кнопок!  
2.Различные префиксы, это то как будет начинаться та или иная кнопка. По дефолту у next - n_, back - b_, page - p_  
3.func_name это то как будет браться имя кнопки, и func_callback соответсвтенно callback_data  
4.Остально довольно понятно!  


Фичи:
1.Вместо call.data.split() можно передать в cur_page сразу call.data -> он будет отформатирован.
