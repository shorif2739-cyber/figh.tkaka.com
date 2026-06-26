<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ফ্রি ফায়ার টুর্নামেন্ট রেজিস্ট্রেশন</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        body {
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.8)), url('https://unsplash.com') no-repeat center center/cover;
            color: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            background: rgba(20, 20, 20, 0.85);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 0 25px #ff4500;
            width: 100%;
            max-width: 450px;
            border: 2px solid #ff4500;
        }
        h2 {
            text-align: center;
            margin-bottom: 20px;
            color: #ff4500;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
            color: #ccc;
        }
        input, select {
            width: 100%;
            padding: 12px;
            border: 1px solid #444;
            background: #222;
            color: #fff;
            border-radius: 8px;
            font-size: 16px;
            outline: none;
            transition: 0.3s;
        }
        input:focus, select:focus {
            border-color: #ff4500;
            box-shadow: 0 0 8px rgba(255, 69, 0, 0.5);
        }
        .extra-player-box {
            background: rgba(255, 69, 0, 0.05);
            padding: 12px;
            border-radius: 8px;
            border-left: 3px solid #ff4500;
            margin-bottom: 15px;
            display: none; /* সিএসএস দিয়ে প্রাথমিক লুকাানো */
        }
        .fee-box {
            background: #ff4500;
            color: white;
            padding: 12px;
            border-radius: 8px;
            text-align: center;
            font-weight: bold;
            margin-bottom: 15px;
            font-size: 16px;
            box-shadow: 0 0 10px rgba(255, 69, 0, 0.3);
        }
        .btn {
            width: 100%;
            padding: 12px;
            background: #ff4500;
            border: none;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s;
            text-transform: uppercase;
            margin-top: 10px;
        }
        .btn:hover {
            background: #ff6a00;
            box-shadow: 0 0 15px #ff4500;
        }
        .success-msg {
            display: none;
            background: #28a745;
            color: white;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            margin-top: 15px;
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>FF Tournament</h2>
    <form id="regForm">
        <div class="form-group">
            <label for="playerName">লিডারের নাম (Player 1 IGN)</label>
            <input type="text" id="playerName" placeholder="যেমন: OP_BOT_99" required>
        </div>
        <div class="form-group">
            <label for="playerUID">লিডারের UID (Player 1 ID)</label>
            <input type="number" id="playerUID" placeholder="যেমন: 123456789" required>
        </div>
        <div class="form-group">
            <label for="teamName">টিমের নাম (Solo হলে নিজের নাম)</label>
            <input type="text" id="teamName" placeholder="যেমন: Team BD Warriors" required>
        </div>
        <div class="form-group">
            <label for="matchType">ম্যাচ টাইপ</label>
            <select id="matchType">
                <option value="Solo">Solo (একক) - ২০ ৳</option>
                <option value="Duo">Duo (দ্বৈত) - ৪০ ৳</option>
                <option value="Squad">Squad (চারজন) - ৮০ ৳</option>
            </select>
        </div>

        <!-- ২য় প্লেয়ার বক্স -->
        <div id="player2_box" class="extra-player-box">
            <div class="form-group">
                <label>২য় প্লেয়ারের নাম ও UID</label>
                <input type="text" id="p2_info" placeholder="যেমন: Name - 12345678">
            </div>
        </div>

        <!-- ৩য় ও ৪র্থ প্লেয়ার বক্স -->
        <div id="squad_boxes" class="extra-player-box">
            <div class="form-group">
                <label>৩য় প্লেয়ারের নাম ও UID</label>
                <input type="text" id="p3_info" placeholder="যেমন: Name - 12345678">
            </div>
            <div class="form-group">
                <label>৪র্থ প্লেয়ারের নাম ও UID</label>
                <input type="text" id="p4_info" placeholder="যেমন: Name - 12345678">
            </div>
        </div>
        
        <!-- ডায়নামিক এন্ট্রি ফি বক্স -->
        <div class="fee-box" id="feeDisplay">
            💵 আপনার এন্ট্রি ফি: ২০ টাকা
        </div>

        <div class="form-group">
            <label for="trxID">এন্ট্রি ফি পাঠান (বিকাশ/নগদ: 01636612855)</label>
            <input type="text" id="trxID" placeholder="বিকাশের ১০ অক্ষর বা নগদের ৮ অক্ষরের TxID দিন" required>
        </div>

        <button type="submit" class="btn">রেজিস্ট্রেশন করুন</button>
    </form>

    <div class="success-msg" id="successMessage">
        🎉 রেজিস্ট্রেশন সফল হয়েছে! বিস্তারিত তথ্যের জন্য অপেক্ষা করুন।
    </div>
</div>

<script>
    // মোবাইল ব্রাউজার ফ্রেন্ডলি আধুনিক সিলেক্টর লজিক
    const matchTypeSelect = document.getElementById('matchType');
    const p2Box = document.getElementById('player2_box');
    const squadBoxes = document.getElementById('squad_boxes');
    const feeDisplay = document.getElementById('feeDisplay');

    matchTypeSelect.addEventListener('change', function() {
        const type = matchTypeSelect.value;

        if (type === "Solo") {
            p2Box.style.display = "none";
            squadBoxes.style.display = "none";
            feeDisplay.innerText = "💵 আপনার এন্ট্রি ফি: ২০ টাকা";
        } else if (type === "Duo") {
            p2Box.style.display = "block";
            squadBoxes.style.display = "none";
            feeDisplay.innerText = "💵 আপনার এন্ট্রি ফি: ৪০ টাকা";
        } else if (type === "Squad") {
            p2Box.style.display = "block";
            squadBoxes.style.display = "block";
            feeDisplay.innerText = "💵 আপনার এন্ট্রি ফি: ৮০ টাকা";
        }
    });

    // ফর্ম সাবমিট প্রসেস
    document.getElementById('regForm').addEventListener('submit', function(e) {
        e.preventDefault(); 
        
        const name = document.getElementById('playerName').value;
        const uid = document.getElementById('playerUID').value;
        const team = document.getElementById('teamName').value;
        const type = matchTypeSelect.value;
        const trx = document.getElementById('trxID').value.trim();
        
        const p2 = document.getElementById('p2_info').value || "N/A";
        const p3 = document.getElementById('p3_info').value || "N/A";
        const p4 = document.getElementById('p4_info').value || "N/A";

        if (trx.length !== 10 && trx.length !== 8) {
            alert("❌ ভুল ট্রানজেকশন আইডি! বিকাশের আইডি ১০ অক্ষরের এবং নগদের আইডি ৮ অক্ষরের হয়। সঠিকভাবে দেখে আবার লিখুন।");
            return false;
        }

        const botToken = "8983954052:AAHweYvtxBX8qLpmotw8fRJo3oApB66lLXc"; 
        const chatId = "7225747767"; 

        let payableAmount = "২০ ৳";
        if (type === "Duo") payableAmount = "৪০ ৳";
        if (type === "Squad") payableAmount = "৮০ ৳";

        let message = `🎮 *নতুন পেইড রেজিস্ট্রেশন* 🎮\n\n`;
        message += `👤 লিডার: ${name}\n🆔 UID: ${uid}\n🛡️ টিম: ${team}\n⚔️ টাইপ: ${type}\n💰 ফি: ${payableAmount}\n`;
        
        if (type === "Duo") {
            message += `👥 প্লেয়ার ২: ${p2}\n`;
        } else if (type === "Squad") {
            message += `👥 প্লেয়ার ২: ${p2}\n👥 প্লেয়ার ৩: ${p3}\n👥 প্লেয়ার ৪: ${p4}\n`;
        }
        
        message += `💵 TxID: ${trx}`;

        fetch(`https://telegram.org{botToken}/sendMessage`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                chat_id: chatId,
                text: message,
                parse_mode: 'Markdown'
            })
        }).then(() => {
            document.getElementById('regForm').style.display = 'none';
            document.getElementById('successMessage').style.display = 'block';
        }).catch(err => {
            alert("কোনো সমস্যা হয়েছে! আবার চেষ্টা করুন।");
        });
    });
</script>
</body>
</html>