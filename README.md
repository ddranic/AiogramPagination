# AioPagination
---
**AioPagination** - library for simpling making pagination (InlineButtons pages) using **aiogram** library, made by [@mrrooooopert](https://t.me/mrrooooopert).

---
### Usage

```
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    pagination = InlinePagination(button_datas=[(i, 2) for i in range(1, 100)], width=4)
    kb = pagination.get_page_keyboard(cur_page=1)

    await message.answer("Hello!", reply_markup=kb)
```
This is a simple example of the library. Let's run through all pagintaion types:
+ InlinePagination
+ ReplyPagination `(not realised yet)`
---
#### InlinePagination class arguments:
+ button_datas - list of iterable items (calback_data, button_name)
+ func_name - func getting name of button by index
+ func_callback - func getting callback_data of button by index
+ callback/back/next/page_prefix - what from will callback_data start
+ width/height is number of rows and columns in every page
+ page_button - string pattern to show current page
---
#### InlinePagination Features:
+ You dont need to split `call.data`, just make `cur_page=call.data` and it will be formatted. 
 
##### Here is an example.
```
@dp.callback_query_handler(lambda c: c.data.startswith("n_"))
async def next(call: types.CallbackQuery):
    pagination = InlinePagination(button_datas=[(i, 2) for i in range(1, 100)], width=4)
    kb = pagination.get_page_keyboard(cur_page=call.data)

    await call.message.edit_reply_markup(reply_markup=kb)
```
