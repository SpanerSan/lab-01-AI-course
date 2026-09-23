"""Parallel test corpus for Lab 01.

The same three items in English, Russian and Kazakh. Parallel meaning is the
point: any difference in token count is a property of the tokenizer, not of
what is being said.

Instructors: the Kazakh and Russian wordings are a starting point. Substitute
your own if you prefer -- but keep the three versions semantically parallel,
otherwise the comparison measures translation length instead of tokenization.
"""

from __future__ import annotations

from typing import Dict

LANGUAGES = ("en", "ru", "kk")

#: One sentence. Short enough to inspect token by token.
SENTENCE: Dict[str, str] = {
    "en": "The bank raised interest rates by two percentage points last quarter.",
    "ru": "Банк повысил процентные ставки на два процентных пункта в прошлом квартале.",
    "kk": "Банк өткен тоқсанда пайыздық мөлшерлемені екі пайыздық тармаққа көтерді.",
}

#: A realistic support request -- the kind of text a production system pays for
#: thousands of times a day.
COMPLAINT: Dict[str, str] = {
    "en": (
        "Good afternoon. I opened a deposit at your branch in March and was told "
        "the rate was fixed for twelve months. In August the rate on my account "
        "dropped without any notice. I have attached the contract and the "
        "statement. Please explain on what basis the rate was changed and "
        "restore the original terms."
    ),
    "ru": (
        "Добрый день. Я открыл депозит в вашем отделении в марте, и мне сказали, "
        "что ставка зафиксирована на двенадцать месяцев. В августе ставка по "
        "моему счёту снизилась без какого-либо уведомления. Прилагаю договор и "
        "выписку. Прошу объяснить, на каком основании была изменена ставка, и "
        "восстановить первоначальные условия."
    ),
    "kk": (
        "Қайырлы күн. Мен наурыз айында сіздің бөлімшеңізде депозит аштым, маған "
        "мөлшерлеме он екі айға бекітілген деп айтылды. Тамыз айында менің "
        "шотымдағы мөлшерлеме ешқандай хабарламасыз төмендеді. Шартты және "
        "үзінді көшірмені қоса тіркеп отырмын. Мөлшерлеме қандай негізде "
        "өзгертілгенін түсіндіріп, бастапқы шарттарды қалпына келтіруіңізді "
        "сұраймын."
    ),
}

#: A system prompt -- the part you resend on every single request.
SYSTEM_PROMPT: Dict[str, str] = {
    "en": (
        "You are a support assistant for a retail bank. Answer only from the "
        "documents provided. If the answer is not in them, say so. Never invent "
        "an account number, a rate or a date."
    ),
    "ru": (
        "Вы — ассистент поддержки розничного банка. Отвечайте только по "
        "предоставленным документам. Если ответа в них нет, так и скажите. "
        "Никогда не выдумывайте номер счёта, ставку или дату."
    ),
    "kk": (
        "Сіз — бөлшек банктің қолдау көрсету ассистентісіз. Тек берілген "
        "құжаттар бойынша жауап беріңіз. Егер жауап оларда болмаса, солай деп "
        "айтыңыз. Шот нөмірін, мөлшерлемені немесе күнді ешқашан ойдан "
        "шығармаңыз."
    ),
}

# Core extension 1: one additional, semantically parallel support complaint.
OWN_COMPLAINT: Dict[str, str] = {
    "en": (
        "Hello. Yesterday I transferred 25,000 tenge through the mobile app. "
        "The money left my account, but the recipient did not receive it. "
        "Please check the payment status and tell me when the transfer will "
        "be completed."
    ),
    "ru": (
        "Здравствуйте. Вчера я перевёл 25 000 тенге через мобильное приложение. "
        "Деньги списались с моего счёта, но получатель их не получил. Пожалуйста, "
        "проверьте статус платежа и сообщите, когда перевод будет завершён."
    ),
    "kk": (
        "Сәлеметсіз бе. Кеше мобильді қосымша арқылы 25 000 теңге аудардым. "
        "Ақша менің шотымнан есептен шығарылды, бірақ алушыға түспеді. Төлем "
        "мәртебесін тексеріп, аударым қашан аяқталатынын хабарлаңыз."
    ),
}

# Core extension 2: the Kazakh versions are similar in length. The first uses
# only Cyrillic letters shared with Russian; the second deliberately contains
# all nine Kazakh-specific letters: ә, ғ, қ, ң, ө, ұ, ү, һ, і.
KK_SHARED_LETTERS: Dict[str, str] = {
    "en": "Arman and Dana are writing an answer in Russian this evening.",
    "ru": "Арман и Дана сегодня вечером пишут ответ на русском языке.",
    "kk": "Арман мен Дана осы кеште орысша жауап жазып отыр.",
}

KK_SPECIFIC_LETTERS: Dict[str, str] = {
    "en": "Galym brought Kundyz and Gauhar a poem today.",
    "ru": "Галым сегодня принёс Кундыз и Гаухар стихотворение.",
    "kk": "Ғалым Құндыз бен Гауһарға бүгін өлең әкелді.",
}

# Core extension 3: the same facts and request as COMPLAINT, represented as
# JSON. ASCII field names are intentionally kept the same in all languages.
COMPLAINT_JSON: Dict[str, str] = {
    "en": (
        '{"greeting": "Good afternoon.", '
        '"deposit": "I opened a deposit at your branch in March.", '
        '"rate_promise": "I was told the rate was fixed for twelve months.", '
        '"change": "In August the rate on my account dropped without any notice.", '
        '"attachments": ["I have attached the contract.", '
        '"I have attached the statement."], '
        '"requests": ["Please explain on what basis the rate was changed.", '
        '"Please restore the original terms."]}'
    ),
    "ru": (
        '{"greeting": "Добрый день.", '
        '"deposit": "Я открыл депозит в вашем отделении в марте.", '
        '"rate_promise": "Мне сказали, что ставка зафиксирована на двенадцать месяцев.", '
        '"change": "В августе ставка по моему счёту снизилась без какого-либо уведомления.", '
        '"attachments": ["Прилагаю договор.", "Прилагаю выписку."], '
        '"requests": ["Прошу объяснить, на каком основании была изменена ставка.", '
        '"Прошу восстановить первоначальные условия."]}'
    ),
    "kk": (
        '{"greeting": "Қайырлы күн.", '
        '"deposit": "Мен наурыз айында сіздің бөлімшеңізде депозит аштым.", '
        '"rate_promise": "Маған мөлшерлеме он екі айға бекітілген деп айтылды.", '
        '"change": "Тамыз айында менің шотымдағы мөлшерлеме ешқандай хабарламасыз төмендеді.", '
        '"attachments": ["Шартты қоса тіркеп отырмын.", '
        '"Үзінді көшірмені қоса тіркеп отырмын."], '
        '"requests": ["Мөлшерлеме қандай негізде өзгертілгенін түсіндіріңіз.", '
        '"Бастапқы шарттарды қалпына келтіріңіз."]}'
    ),
}

#: Everything the lab measures, keyed by a short id.
CORPUS: Dict[str, Dict[str, str]] = {
    "sentence": SENTENCE,
    "complaint": COMPLAINT,
    "system_prompt": SYSTEM_PROMPT,
    "own_complaint": OWN_COMPLAINT,
    "kk_shared_letters": KK_SHARED_LETTERS,
    "kk_specific_letters": KK_SPECIFIC_LETTERS,
    "complaint_json": COMPLAINT_JSON,
}
