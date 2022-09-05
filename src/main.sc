require: slotfilling/slotFilling.sc
  module = sys.zb-common
theme: /

    state: Start
        q!: $regex</start>
        a: Начнём.

    state: Hello
        q!: *(привет*/здравствуй*/добр*)*
        a: Привет, я чат-бот Наташи
        go!: /WhatsUp
        
    state: WhatsUp
        a: Как дела?  
        
        state: Great
            q: *(отлично/супер/замечательно/великолепно)*
            a: Я рад за Вас, у хорошего человека дела плохи не бывают!
        
        state: Good
            q: *(хорош*/норм*)*
            a: Я рад за Вас, все лучшее - впереди!
        
        state: Bad
            q: *(плох*/не(очень/хорош*))*
            a: Не стоит из-за этого грустить. Терпения Вам!    

    state: /HowAreYou
        q: *(как (ты/твои*))*
        a: Все замечательно! Когда нечем думать, проблем не возникает.
        
    state: Bye
        intent!: /пока
        a: Пока, мой милый друг. Возвращайся!

    state: NoMatch
        event!: noMatch
        a: Я не понял. Вы сказали: {{$request.query}}

    state: Match
        event!: match
        a: {{$context.intent.answer}}