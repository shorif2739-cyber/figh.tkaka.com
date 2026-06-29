<!doctype html>
<html lang="bn">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>ফ্রি ফায়ার টুর্নামেন্ট রেজিস্ট্রেশন</title>
  <style>
    *{margin:0;padding:0;box-sizing:border-box;font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif}
    body{background:linear-gradient(rgba(0,0,0,.7),rgba(0,0,0,.8)), url('https://source.unsplash.com/1600x900/?gaming') no-repeat center center/cover;color:#fff;display:flex;justify-content:center;align-items:center;min-height:100vh;padding:20px}
    .container{background:rgba(20,20,20,.95);padding:30px;border-radius:12px;box-shadow:0 0 25px #ff4500;width:100%;max-width:520px;border:1px solid rgba(255,69,0,.15)}
    h2{text-align:center;margin-bottom:20px;color:#ff4500;text-transform:uppercase;letter-spacing:2px}
    .form-group{margin-bottom:12px}
    label{display:block;margin-bottom:6px;font-weight:600;color:#ddd}
    input,select{width:100%;padding:10px;border:1px solid #444;background:#171717;color:#fff;border-radius:8px;font-size:15px;outline:none;transition:.18s}
    input:focus,select:focus{border-color:#ff4500;box-shadow:0 0 8px rgba(255,69,0,.2)}
    .extra-players{background:rgba(255,69,0,.03);padding:10px;border-radius:8px;border-left:3px solid #ff4500;margin-top:8px;display:none}
    .fee-box{background:#ff4500;color:white;padding:12px;border-radius:8px;text-align:center;font-weight:700;margin-bottom:12px;font-size:15px}
    .btn{width:100%;padding:12px;background:#ff4500;border:none;color:white;font-size:17px;font-weight:700;border-radius:8px;cursor:pointer;transition:.18s;text-transform:uppercase}
    .btn:disabled{opacity:.7;cursor:not-allowed}
    .btn:hover{background:#ff6a00}
    .success-msg{display:none;background:#28a745;color:white;padding:12px;border-radius:8px;text-align:center;margin-top:12px;font-weight:700}
    .error-msg{display:none;background:#dc3545;color:white;padding:10px;border-radius:8px;text-align:center;margin-top:10px}
    small.hint{color:#cfcfcf}
  </style>
</head>
<body>
  <div class="container" role="main" aria-labelledby="title">
    <h2 id="title">FF Tournament</h2>
    <form id="regForm" novalidate>
      <div class="form-group">
        <label for="playerName">লিডারের নাম (Player 1 IGN)</label>
        <input type="text" id="playerName" name="playerName" placeholder="যেমন: OP_BOT_99" required minlength="2" />
      </div>

      <div class="form-group">
        <label for="playerUID">লিডারের UID (Player 1 ID)</label>
        <input type="text" id="playerUID" name="playerUID" placeholder="যেমন: 123456789" required pattern="^\d{4,12}$" />
        <small class="hint">UID সাধারণত ডিজিট; 4–12 সংখ্যার মধ্যে দিন</small>
      </div>

      <div class="form-group">
        <label for="teamName">টিমের নাম (Solo হলে নিজের নাম)</label>
        <input type="text" id="teamName" name="teamName" placeholder="যেমন: Team BD Warriors" required />
      </div>

      <div class="form-group">
        <label for="matchType">ম্যাচ টাইপ</label>
        <select id="matchType" name="matchType" onchange="togglePlayers()" aria-controls="player2_box squad_boxes" required>
          <option value="Solo">Solo (একক) - ২০ ৳</option>
          <option value="Duo">Duo (দ্বৈত) - ৪০ ৳</option>
          <option value="Squad">Squad (চারজন) - ৮০ ৳</option>
        </select>
      </div>

      <div id="player2_box" class="extra-players" aria-hidden="true">
        <div class="form-group">
          <label for="p2_info">২য় প্লেয়ারের নাম ও UID</label>
          <input type="text" id="p2_info" name="p2_info" placeholder="নাম - UID লিখুন" />
        </div>
      </div>

      <div id="squad_boxes" class="extra-players" aria-hidden="true">
        <div class="form-group">
          <label for="p3_info">৩য় প্লেয়ারের নাম ও UID</label>
          <input type="text" id="p3_info" name="p3_info" placeholder="নাম - UID লিখুন" />
        </div>
        <div class="form-group">
          <label for="p4_info">৪র্থ প্লেয়ারের নাম ও UID</label>
          <input type="text" id="p4_info" name="p4_info" placeholder="নাম - UID লিখুন" />
        </div>
      </div>

      <div class="fee-box" id="feeDisplay" aria-live="polite">💵 আপনার এন্ট্রি ফি: ২০ টাকা</div>

      <div class="form-group">
        <label for="trxID">এন্ট্রি ফি TxID পাঠান (বিকাশ/নগদ)</label>
        <input type="text" id="trxID" name="trxID" placeholder="বিকাশ: 10 অক্ষর, নগদ: 8 অক্ষর" required pattern="^[A-Za-z0-9]{8,10}$" />
        <small class="hint">TxID শুধুমাত্র অক্ষর/সংখ্যা; 8 অথবা 10 অক্ষর</small>
      </div>

      <button type="submit" class="btn" id="submitBtn">রেজিস্ট্রেশন করুন</button>
    </form>

    <div class="success-msg" id="successMessage" role="status">🎉 রেজিস্ট্রেশন সফল হয়েছে! বিস্তারিত তথ্যের জন্য অপেক্ষা করুন।</div>
    <div class="error-msg" id="errorMessage" role="alert"></div>
  </div>

  <script>
    // পরিবহিত করুন: যদি সার্ভার একই হোস্টে হয়, এ রিলেটিভ পথ ঠিক থাকবে.
    // যদি আলাদা সার্ভারে দেন, এখানে সেট করুন: e.g. "https://example.com/api/register"
    const API_URL = "/api/register";

    function togglePlayers() {
      const type = document.getElementById('matchType').value;
      const p2Box = document.getElementById('player2_box');
      const squadBoxes = document.getElementById('squad_boxes');
      const feeDisplay = document.getElementById('feeDisplay');

      if (type === "Solo") {
        p2Box.style.display = "none"; p2Box.setAttribute('aria-hidden','true');
        squadBoxes.style.display = "none"; squadBoxes.setAttribute('aria-hidden','true');
        feeDisplay.innerText = "💵 আপনার এন্ট্রি ফি: ২০ টাকা";
      } else if (type === "Duo") {
        p2Box.style.display = "block"; p2Box.setAttribute('aria-hidden','false');
        squadBoxes.style.display = "none"; squadBoxes.setAttribute('aria-hidden','true');
        feeDisplay.innerText = "💵 আপনার এন্ট্রি ফি: ৪০ টাকা";
      } else {
        p2Box.style.display = "block"; p2Box.setAttribute('aria-hidden','false');
        squadBoxes.style.display = "block"; squadBoxes.setAttribute('aria-hidden','false');
        feeDisplay.innerText = "💵 আপনার এন্ট্রি ফি: ৮০ টাকা";
      }
    }

    document.addEventListener('DOMContentLoaded', () => { togglePlayers(); });

    function showError(msg) {
      const el = document.getElementById('errorMessage');
      el.innerText = msg;
      el.style.display = 'block';
      window.scrollTo({top:0,behavior:'smooth'});
      setTimeout(()=>{ el.style.display='none'; },8000);
    }

    document.getElementById('regForm').addEventListener('submit', async function(e) {
      e.preventDefault();
      if (!this.checkValidity()) { showError("অনুগ্রহ করে সব তথ্য সঠিকভাবে পূরণ করুন।"); return; }

      const name = document.getElementById('playerName').value.trim();
      const uid = document.getElementById('playerUID').value.trim();
      const team = document.getElementById('teamName').value.trim();
      const type = document.getElementById('matchType').value;
      const trx = document.getElementById('trxID').value.trim().toUpperCase();
      const p2 = document.getElementById('p2_info').value.trim() || "N/A";
      const p3 = document.getElementById('p3_info').value.trim() || "N/A";
      const p4 = document.getElementById('p4_info').value.trim() || "N/A";

      if (!/^[A-Z0-9]{8,10}$/i.test(trx)) { showError("❌ ভুল TxID ফরম্যাট — 8 বা 10 অক্ষরের অ্যালফানিউমেরিক ব্যবহার করুন।"); return; }

      const payload = { name, uid, team, type, trx, players:{ p2, p3, p4 } };

      const submitBtn = document.getElementById('submitBtn');
      submitBtn.disabled = true;
      submitBtn.innerText = 'পাঠানো হচ্ছে...';

      try {
        const res = await fetch(API_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
          credentials: 'omit'
        });

        if (res.status === 409) {
          const txt = await res.text().catch(()=>"Duplicate TxID");
          throw new Error(txt || "Duplicate TxID");
        }
        if (!res.ok) {
          const txt = await res.text().catch(()=>null);
          throw new Error(txt || `সার্ভার ত্রুটি: ${res.status}`);
        }

        document.getElementById('regForm').style.display = 'none';
        document.getElementById('successMessage').style.display = 'block';
      } catch (err) {
        console.error(err);
        showError("কোনো সমস্যা হয়েছে: " + (err.message || "আবার চেষ্টা করুন।"));
      } finally {
        submitBtn.disabled = false;
        submitBtn.innerText = 'রেজিস্ট্রেশন করুন';
      }
    });
  </script>
</body>
</html>