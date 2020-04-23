$(function () {
    $(window).on('scroll', function () {
        if ($(window).scrollTop() > 10) {
            $('.navbar').addClass('active');
        } else {
            $('.navbar').removeClass('active');
        }
    });

    function encodeHtml(s) {
        return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
    }

    function getCurrentTime() {
        var dt = new Date(); 
        return `${formatAMPM(dt)} | ${dt.getDay()} ${Date.shortMonths[dt.getMonth()]}`;
    }

    Date.shortMonths = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    function formatAMPM(date) {
        // https://stackoverflow.com/questions/8888491/how-do-you-display-javascript-datetime-in-12-hour-am-pm-format
        var hours = date.getHours();
        var minutes = date.getMinutes();
        var ampm = hours >= 12 ? 'PM' : 'AM';
        hours = hours % 12;
        hours = hours ? hours : 12; // the hour '0' should be '12'
        minutes = minutes < 10 ? '0'+minutes : minutes;
        var strTime = hours + ':' + minutes + ' ' + ampm;
        return strTime;
    }

    const Templates = {
        Messages: {
            Mine: (Date, Message) => $('<div></div>').html(`
                    <div class="media w-50 ml-auto mb-3">
                        <div class="media-body">
                            <div class="bg-primary rounded py-2 px-3 mb-2">
                                <p class="text-small mb-0 text-white">${encodeHtml(Message)}</p>
                            </div>
                            <p class="small text-muted">${Date}</p>
                        </div>
                    </div>
                `),
            Bot: (Date, Message) => $('<div></div>').html(`
                    <!-- Sender Message-->
                    <div class="media w-50 mb-3"><img
                            src="assets/logo-small.jpg"
                            alt="user" width="50" class="rounded-circle">
                        <div class="media-body ml-3">
                            <div class="bg-light rounded py-2 px-3 mb-2">
                                <p class="text-small mb-0 text-muted">${encodeHtml(Message)}</p>
                            </div>
                            <p class="small text-muted">${Date}</p>
                        </div>
                    </div>
                `)
        }
    }

    let $form       = $("#frmChatPost");
    let $txtMessage = $('#txtMessage');
    let $btnSend    = $form.find('button');
    let $botChat    = $('#bot-chat');
    $botChat.animate( { scrollTop: $botChat.prop("scrollHeight") }, "slow" );

    // Stop form from posting
    $form.on("submit", () => false);

    function sendMessage() {
        // Check if empty
        if ( $txtMessage.val().trim() == '' )
            return;

        let sendDate = getCurrentTime();
        var userMessage = $txtMessage.val(); // Get our message
        $txtMessage.val("");                 // Reset the textbox

        // Add our chat message
        $botChat.append(Templates.Messages.Mine(sendDate, userMessage));
        $botChat.animate( { scrollTop: $botChat.prop("scrollHeight") }, "slow" );

        $.ajax({
            url: 	"/chatbot/generate",
            method: "post",
            dataType: "json",
            data: { message: userMessage },

            success(data, textStatus, jqXHR) {
                let recvDate = getCurrentTime();

                console.log(data, data.message.length);
                var botMessage = data.message;
                //var botProbability = data.probability;
                
                if (Array.isArray(botMessage)) {
                    for (const msg of botMessage) {
                        $botChat.append(Templates.Messages.Bot(recvDate, msg));
                    }
                } else {
                    $botChat.append(Templates.Messages.Bot(recvDate, botMessage));
                }

                $botChat.animate( { scrollTop: $botChat.prop("scrollHeight") }, "slow" );
            },

            error(jqXHR, textStatus, errorThrown) {
                console.error(jqXHR, textStatus, errorThrown);
            }
        });
    }

    // On send button pressed
    $btnSend.on('click', function() {
        sendMessage();
    });


    // On enter pressed
    $txtMessage.keypress(function(e) {
        // If enter key is pressed
        if (e.which == 13) {
            sendMessage();
        }
    });
});