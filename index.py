# LIBRARIES
import asyncio
import logging
import sys
import random
import time
import threading
from aiogram import Bot, Dispatcher, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import FSInputFile
from aiogram import F
import aiogram.utils.markdown as fmt
from config import settings 

# API
TOKEN = settings['token']
dp = Dispatcher()

###################
###### START ######
###################

@dp.message(Command("start"))
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="📃 Информация"))
    builder.row(types.KeyboardButton(text="🎖️ Ветераны"))
    builder.row(types.KeyboardButton(text="📚 Книги ВОВ [СКОРО]"))
    
    await message.reply(
        fmt.text(
            fmt.text(f"👋 Привет, <b>{message.from_user.first_name}</b>", "\n\nВыберите интересующую вас информацию 👇"),
        ), parse_mode="HTML", reply_markup=builder.as_markup(resize_keyboard=True)
    )

@dp.message(F.text == '↩️ Назад (Главное меню)')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="📃 Информация"))
    builder.row(types.KeyboardButton(text="🎖️ Ветераны"))
    builder.row(types.KeyboardButton(text="📚 Книги ВОВ [СКОРО]"))
    
    await message.reply(
        fmt.text(
            fmt.text(f"Выберите интересующую вас информацию 👇"),
        ), parse_mode="HTML", reply_markup=builder.as_markup(resize_keyboard=True)
    )

@dp.message(F.text == '📃 Информация')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    
    builder.row(types.KeyboardButton(text="↩️ Назад (Главное меню)"))

    image_from_pc = FSInputFile("src/main/Picture.png")
    

    await message.answer_photo(image_from_pc,caption="<b>Участие жителей Анабарского улуса в Великой Отечественной Войне</b>\n\nНа территории Анабарского улуса никогда не было военных действий, как не было их и на огромных пространствах Якутии. Но война вошла в каждый улус, в каждую семью республики – голодом, карточной системой обеспечения продуктами, почти круглосуточным трудом.\nСоветский Союз не призывал на фронт представителей коренных малых народов Севера, уходили на войну отдельные добровольцы. Но все население поголовно работало для фронта с напряжением всех сил. \nВ общей сложности, Анабарский улус собрал и отправил фронту:\n- денежных средств – 264 980 рублей,\n- теплых вещей – 5858 шт.,\n- на строительство танка «Советская Якутия» - 196 007 рублей.", reply_markup=builder.as_markup(resize_keyboard=True))

@dp.message(F.text == '🎖️ Ветераны')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="Андросова Федора Николаевна"))
    builder.row(types.KeyboardButton(text="Андросова Марфа Михайловна"))
    builder.row(types.KeyboardButton(text="Андросова Мария Михайловна"))
    builder.row(types.KeyboardButton(text="Андросова Евдокия Васильевна"))
    builder.row(types.KeyboardButton(text="Андросова Варвара Федоровна"))
    builder.row(types.KeyboardButton(text="Акакиева Софья Павловна"))
    builder.row(types.KeyboardButton(text="Акакиева Татьяна Егоровна"))
    builder.row(types.KeyboardButton(text="Анисимов Егор Иннокентьевич"))
    builder.row(types.KeyboardButton(text="Анисимова Татьяна Федоровна"))
    builder.row(types.KeyboardButton(text="Антонов Никифор Филиппович"))
    builder.row(types.KeyboardButton(text="Арьянова Екатерина Алексеевна"))
    builder.row(types.KeyboardButton(text="Арьянов Иван Васильевич"))
    builder.row(types.KeyboardButton(text="Борисова Мавра Ивановна"))
    builder.row(types.KeyboardButton(text="Винокурова Екатерина"))
    builder.row(types.KeyboardButton(text="Винокуров Николай Иннокентьевич"))
    builder.row(types.KeyboardButton(text="Винокуров Константин Николаевич"))
    builder.row(types.KeyboardButton(text="Винокуров Дмитрий Егорович"))
    builder.row(types.KeyboardButton(text="Винокуров Василий Николаевич"))
    builder.row(types.KeyboardButton(text="Винокуров Егор Романович"))
    builder.row(types.KeyboardButton(text="↩️ Назад (Главное меню)"))
    
    await message.reply(
        fmt.text(
            fmt.text(f"👋 Привет, <b>{message.from_user.first_name}</b>", "\n\nВыберите ветерана 👇"),
        ), parse_mode="HTML", reply_markup=builder.as_markup(resize_keyboard=True)
    )

@dp.message(F.text == '↩️ Назад (Ветераны)')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="Андросова Федора Николаевна"))
    builder.row(types.KeyboardButton(text="Андросова Марфа Михайловна"))
    builder.row(types.KeyboardButton(text="Андросова Мария Михайловна"))
    builder.row(types.KeyboardButton(text="Андросова Евдокия Васильевна"))
    builder.row(types.KeyboardButton(text="Андросова Варвара Федоровна"))
    builder.row(types.KeyboardButton(text="Акакиева Софья Павловна"))
    builder.row(types.KeyboardButton(text="Акакиева Татьяна Егоровна"))
    builder.row(types.KeyboardButton(text="Анисимов Егор Иннокентьевич"))
    builder.row(types.KeyboardButton(text="Анисимова Татьяна Федоровна"))
    builder.row(types.KeyboardButton(text="Антонов Никифор Филиппович"))
    builder.row(types.KeyboardButton(text="Арьянова Екатерина Алексеевна"))
    builder.row(types.KeyboardButton(text="Арьянов Иван Васильевич"))
    builder.row(types.KeyboardButton(text="Борисова Мавра Ивановна"))
    builder.row(types.KeyboardButton(text="Винокурова Екатерина"))
    builder.row(types.KeyboardButton(text="Винокуров Николай Иннокентьевич"))
    builder.row(types.KeyboardButton(text="Винокуров Константин Николаевич"))
    builder.row(types.KeyboardButton(text="Винокуров Дмитрий Егорович"))
    builder.row(types.KeyboardButton(text="Винокуров Василий Николаевич"))
    builder.row(types.KeyboardButton(text="Винокуров Егор Романович"))
    builder.row(types.KeyboardButton(text="↩️ Назад (Главное меню)"))
    
    await message.reply(
        fmt.text(
            fmt.text(f"👋 Привет, <b>{message.from_user.first_name}</b>", "\n\nВыберите ветерана 👇"),
        ), parse_mode="HTML", reply_markup=builder.as_markup(resize_keyboard=True)
    )

@dp.message(F.text == 'Андросова Федора Николаевна')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/1.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Андросова Федора Николаевна</b>\n\nМин Андросова Федора Николаевна 1928с. Дьэһэй нэһилиэгин кэргэҥҥэ төроөөбүтүм Саскылаах һ клстаах оскуолатын 1945с. Онтон комсомоллаах этибит онон удьа бөһүолэҕэр ааҕар балаҕан  сэбиэ диссэйинэн үлҥэ ыппыттара. Ол кэнниттэн хас сылын Якутскайга үэрэнэ бара сатаабыппыт ол бириэмэҕэ самолет сылдьыбат этэ, онон кыайан үэрэммэтэхпит. Онтон бибилиотека сэбиэдэссэйинэн үлэлээбтитим, онтон госбаҥҥа операционнай булгалтериинэн үлэлээбитим ол инньитинэн Архивка уонна загсаҕа үлэлээбитим онтон доруобуйабыттан молбо 3 үнэн хас да сылла эттэнэсыльдьыбытым уонна 1975 c. книга  магазиныгар үлэлээбитим онтон  Якутскайга операцияламмытым 1947-5 с с райсоветка эвентутан оҕон талыллабытым  оҕолорун улахан кыыьым библиотекаҕа үлэлиир, орто кыьым инвалид сүрэҕэ операциялаах Кангаласс ботролҥор олорор кэргэннээх 1  оҕолоох кыра уолум Маят диэн экпедия участаҕар үлэлиир Арьянов Александр Егорович. 10 сиэннээхпин 6 оҕо хос сиэннээхпин, бэйэм ол иннитигэр араас быстах үлэлэргэ үлэлии сылдьыбытым.", reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text == 'Андросова Марфа Михайловна')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/2.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Андросова Марфа Михайловна</b>\n\n", reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text == 'Андросова Мария Михайловна')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/3.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Андросова Мария Михайловна</b>\n\n", reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text == 'Андросова Евдокия Васильевна')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/4.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Андросова Евдокия Васильевна</b>\n\n", reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text == 'Андросова Варвара Федоровна')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/5.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Андросова Варвара Федоровна</b>\n\nАндросова Варвара Федоровна 1911 с. Саскылаахка төрөөбүтэ. Билигин үҥ саастаах. Сэрии буоларын саҕана кирииччэ үктүүр этим. Ол сырыттахпытына мунньах буолар диэн, барыбытын ыҥыран ылбыттара. Уонна сэрии буолла диэн иҺитиннэрбиттэрэ истибиппин итэҕэйбэтэҕим. Сэрии созона Саскылаахка кыаммат ыалларга, фроҥҥа ичигэс таҥас, үтүлүк тигэр этибит. Сэрии кэлиитти ас суох этэ. Мин ыксааммын оҕорбор оту хомуйан баран ильдьиритэн биэрэр этим. Сарсырда эрдэттэн киҺээҥҥэ дылы бокуойа суох үлэлиирбит. 7 сылы быһа кирпииччэ үктээбитим. Варвара Федоровна 3 оҕолоох, икки оҕону ииттэ ылбыт. Билигин өолбоөх сиэннэрдээх, хос сэннэрдээх. Улахан уола Саскылаахка пожарнайга улэлиир. Кыыһа больницаҕа поворынан үлэлиир.", reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text == 'Акакиева Софья Павловна')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/6.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Акакиева Софья Павловна</b>\n\nСофья Павловна 1923 сыл, кулун тутар 12 күнүгэр Доруоха учаастагар төрөөбүтэ. Аҕата Павел Николаевич Акакиев булчут, ийэтэ Анна Романовна иистэнньэҥ. 6 эрэ кылаас баар этэ, ол иһин 6 кылаас кэнниттэн, үлэлээн киирэн барбыта. Сэрии сылларыгар районнааҕы балыһаҕа поварынан, онтон Анаабырдааҕы потребобществоҕа  ыанньык сытынан, пекарынан, сааскылаах оскуолатын интернатыгар поварынан өр кэмҥэ эҥкилэ суох үлэлээбитэ. «1941-45сс. А5а дойду Улуу сэриитигэр үлэҕэ килбиэнин иһин»(1994с), «Үлэ ветерана» медалынан наҕараадаламмыта. Сэрии бүппүтүн кэннэ Софья Павловнаҕа тыыл ветеранын аатын иҥэрбиттэр. Күн бүгүҥҥүтүгэр дылы начальнай осколо буфетыгар поварынан үлэлии сылдьар.", reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text == 'Акакиева Татьяна Егоровна')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/7.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Акакиева Татьяна Егоровна</b>\n\nМин 1927 сыллаахха олунньу 8 күнүгэр Сааскылаахха төрөөбүтүм. Төрөппуттэрим, Акакиева Агафья Дмитриевна, аҕам Акакиев Егор Степанович. Биһиги оҕолор 8 этибит, мин саамай кыраларабын. 10 саастаахпар оскуолаҕа киирбитим уонна 44 сыллаахха бүтэрбитим, оччотооҕуга ситэтэ суох 7 кылаастаах этэ. 1948 сыллаахтан 52 сыллаахха дылы балыыһаҕа медсестранан үлэлээбитим, оччотооҕу фельдшердар олус аламаҕай, үлэлэргэр бэриниилээх дьоннор этилэр, эдэр ыччаты үөрэтэллэрэ, бэйэлэригэр тардыллара. Эдэр очакка баҕарыам этэ күн сиригэр төрөөн-үөскээн оллорон иэскитин үтүө суобастаахтык, чиэһинэйдик олорууттан туох кэлиэй. Билигин Чечня сэриитэ бара туорарынан сибээстээн бу сэрии түргэнник тохтууругар, инникитин сэрии буолбатгар диэн баҕарабын.", reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text == 'Анисимов Егор Иннокентьевич')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/8.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Анисимов Егор Иннокентьевич</b>\n\n", reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text == 'Анисимова Татьяна Федоровна')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/9.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Анисимова Татьяна Федоровна</b>\n\nМин 1932 сыллаахха Өлөөн улууһун Дьэлиндэ нэһлиэгэр төрөөбүтүм. 6 сааспар ийэм өлөн оҕо дьиэтигэр интернатка олоро киирбитим. Мин ийэбэр бүтэһик оҕото этим. 1942 сыллаахха төрдүс кылааһы бүтэрэн баран салҕыы Өлөөн орто оскуолатыгар үөрэнэ барбытым. Ол саҕана Өлөөҥҥө табаннан айанаан тиийбиппит. Салҕыы үөрэммитим. Бу ынырыктаах сыллар этэ. Ол саҕана оҕолор улахан дьону кытта тэҥҥэ бириэмэ аахсыбакка үлэлиирбит. Сайынын луук, отон, сугун хомуйан хоскуоска туттарарбыт. 1945с.\n 1953с. Сааскылаахха, райпоҕа кылаабынай поварынан үлэҕэ киирбитим. 1960с госбаҥҥа охраннигынан үлэлээбитим. Ол курдук уопсай үлэм ыстааһа 58 сыл. 1983с. Пенсияҕа тахсыбытым. Ылдьар буолан устунан олоробун. Түөрт оҕолоохпун, сиэннэрдээхпин уонна хос сиэннэр бааллар.", reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text == 'Антонов Никифор Филиппович')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/10.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Антонов Никифор Филиппович</b>\n\n", reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text == 'Арьянова Екатерина Алексеевна')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/11.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Арьянова Екатерина Алексеевна</b>\n\nМин Арьянова Екатерина Алексеевнабын 1932 Сыллаахка Кулун тутар 8 күнүгэр төрөөбүтүм. Төрөөбүт сирим Арыйаан хайата онно дьоннорум сирдэрэ. Онтон 7 сааспар олскуолаҕа киирбитим. 1941 сыллаахка үөрэнэ сырыттахпына сэрии буолубта. Сэрии сылларыгар ньоммутугар көмөлоһөн мас кэрдэн саһааннаан, уонна холкуоска тыс, тирии, имистэ тичистэ, биһиэхэ оскуола оҕолоругар үтүлүк кээнчэ тиктэлэр этилэр. Ас-таҥас кытаанах этэ киилэн 400гр оҕоҕо этэ. Ол үорэнэ сыльдьан ыальдьан оскуолабын ситэ бүтэрбэтэҕим. Дьонмун кытта үлэлии сыльдьыбытым, онтон кэргэн тахсан биэс оҕону төрөөбүтүм, оҕолор билигин бааллла иккитэ ыам сорохтор кэргэнэ суохтар. Сиэннэрим аҕыстар, биир хос сиэннээхпин. Оҕонньорум суох буолбута  биир сылын туолуо, кини эмиэ тыыл ветерана этэ. Билигин үс оҕом биир сиэннээхпин кытта олоробун.", reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text == 'Арьянов Иван Васильевич')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/12.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Арьянов Иван Васильевич</b>\n\n", reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text == 'Борисова Мавра Ивановна')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/13.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Борисова Мавра Ивановна</b>\n\n", reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text == 'Винокурова Екатерина')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/14.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Винокурова Екатерина</b>\n\n", reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text == 'Винокуров Николай Иннокентьевич')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/15.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Винокуров Николай Иннокентьевич</b>\n\n", reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text == 'Винокуров Константин Николаевич')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/16.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Винокуров Константин Николаевич</b>\n\n", reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text == 'Винокуров Дмитрий Егорович')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/17.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Винокуров Дмитрий Егорович</b>\n\n", reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text == 'Винокуров Василий Николаевич')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/18.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Винокуров Василий Николаевич</b>\n\n", reply_markup=builder.as_markup(resize_keyboard=True))
@dp.message(F.text == 'Винокуров Егор Романович')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="↩️ Назад (Ветераны)"))
    image_from_pc = FSInputFile("src/19.jpeg")
    await message.answer_photo(image_from_pc,caption="<b>Винокуров Егор Романович</b>\n\n", reply_markup=builder.as_markup(resize_keyboard=True))

# BOT START
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())