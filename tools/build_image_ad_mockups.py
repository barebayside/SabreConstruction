"""Five Sabre image-ad mockups (1080x1350) modelled on long-running builder ads, rendered to PNG with Edge headless.

Real Sabre photos and Nathan's real video frames only (src/). Offers and prices are DRAFT slots for Nathan.
Rating 4.5 / 12 reviews = client-facts.md (2026-09-05); never round up.
Usage: python tools/build_image_ad_mockups.py <swipe folder>/sabre-mockups
"""
import sys, pathlib, subprocess

M = pathlib.Path(sys.argv[1]).resolve()
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

HEAD = """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0} html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:Figtree,Arial,sans-serif;color:#1B1C1F;position:relative;background:#F8F7F4}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.red{color:#EB2227} .btn{display:inline-block;background:#EB2227;color:#fff;font-weight:700;border-radius:12px;padding:22px 34px;font-size:34px}
.bar{position:absolute;left:0;right:0;bottom:0;height:150px;display:flex;align-items:center;justify-content:space-between;padding:0 48px}
.bar img{height:74px} .fine{position:absolute;font-size:19px;opacity:.8}
.stars{color:#F4B400;font-size:42px;letter-spacing:2px;position:relative;display:inline-block}
.stars .half{position:relative;display:inline-block;color:#d9d9d9} .stars .half:before{content:'\\2605';position:absolute;left:0;width:50%;overflow:hidden;color:#F4B400}
</style></head><body>"""

ADS = {
"1-same-street": """
<img class="bg" src="src/proj2x-clarence.jpg" style="object-position:40% 50%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,16,18,.82) 0%,rgba(15,16,18,.35) 42%,rgba(15,16,18,0) 60%)"></div>
<div style="position:absolute;left:60px;right:60px;top:70px;color:#fff">
 <div style="font-size:24px;letter-spacing:.14em;font-weight:600;opacity:.9">KNOCKDOWN REBUILD · WYNNUM · MANLY · BIRKDALE</div>
 <div style="font-size:92px;font-weight:800;line-height:1.02;margin-top:22px">You picked<br>this street.</div>
 <div style="font-size:46px;font-weight:500;line-height:1.2;margin-top:22px;max-width:900px">Don't let the house decide<br>you have to leave it.</div>
</div>
<div class="bar" style="background:#fff"><img src="src/sabre-logo.png"><span class="btn">Book a walk-through</span></div>
""",
"2-old-new-offer": """
<div style="position:absolute;inset:0;background:linear-gradient(180deg,#cfe3f5,#F8F7F4 40%)"></div>
<div style="position:absolute;top:54px;left:0;right:0;text-align:center">
 <div style="font-size:44px;font-weight:600;font-style:italic">Knock down. Rebuild.</div>
 <div style="font-size:120px;font-weight:900;line-height:1;margin-top:6px">Same street.</div>
 <div style="display:inline-block;margin-top:22px;background:#EB2227;color:#fff;font-weight:800;font-size:46px;padding:14px 30px;border-radius:6px">FREE KITCHEN UPGRADE*</div>
</div>
<div style="position:absolute;left:0;right:0;top:420px;bottom:150px;overflow:hidden">
 <img src="src/kd-17.5.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:62% 60%;clip-path:polygon(58% 0,100% 0,100% 100%,44% 100%)">
 <img src="src/proj2x-clarence.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:30% 50%;clip-path:polygon(0 0,58% 0,44% 100%,0 100%)">
 <div style="position:absolute;top:0;bottom:0;left:50.5%;width:8px;background:#fff;transform:skewX(-7.5deg)"></div>
 <div style="position:absolute;left:28px;top:24px;background:#fff;font-weight:800;font-size:28px;padding:6px 16px;border-radius:6px">THE NEW ONE</div>
 <div style="position:absolute;right:28px;top:24px;background:#1B1C1F;color:#fff;font-weight:800;font-size:28px;padding:6px 16px;border-radius:6px">THE OLD HOUSE</div>
</div>
<div class="bar" style="background:#1B1C1F;color:#fff"><img src="src/sabre-logo-white.png"><span style="font-size:36px;font-weight:700">Get your free block check ›</span></div>
<div class="fine" style="left:24px;bottom:156px;color:#fff;text-shadow:0 1px 3px #000">*Draft offer for Nathan to confirm</div>
""",
"3-price-circle": """
<img class="bg" src="src/proj2x-brighton.jpg" style="object-position:50% 50%;top:430px;height:920px">
<div style="position:absolute;left:0;right:0;top:0;height:460px;background:linear-gradient(180deg,#dcebf7,#eef4f9)"></div>
<div style="position:absolute;left:70px;top:70px;width:640px;height:640px;border-radius:50%;background:#EB2227;color:#fff;text-align:center;padding:100px 70px 0;box-shadow:0 10px 40px rgba(0,0,0,.25)">
 <div style="font-size:50px;font-weight:800;line-height:1.05">Your new<br>family home</div>
 <div style="font-size:36px;font-weight:500;margin-top:8px">on the block you already own</div>
 <div style="margin:22px auto 0;width:400px;border:3px dashed #fff;border-radius:12px;padding:10px;font-size:60px;font-weight:900">From $[ ]*</div>
 <div style="font-size:33px;font-weight:700;margin-top:24px;line-height:1.35">Demolition included*<br>Upgrade pack included*</div>
</div>
<div style="position:absolute;right:56px;top:84px;width:280px;height:280px;border-radius:50%;background:radial-gradient(circle,#f3d27a,#c99a2e);display:flex;align-items:center;justify-content:center;text-align:center;font-weight:800;font-size:34px;line-height:1.15;color:#2b2104;border:8px solid #fff3cf">Building on<br>the Bayside<br>since 1990</div>
<img src="src/sabre-logo.png" style="position:absolute;right:56px;top:410px;height:70px;background:#fff;padding:10px 16px;border-radius:10px">
<div style="position:absolute;left:46px;bottom:60px;width:300px;background:#fff;border-radius:16px;box-shadow:0 8px 30px rgba(0,0,0,.3);text-align:center;padding:22px 16px;transform:rotate(-5deg)">
 <div style="font-size:24px;font-weight:700;color:#EB2227;letter-spacing:.1em">NOW BOOKING</div><div style="font-size:52px;font-weight:900;line-height:1">2027</div><div style="font-size:26px;font-weight:600">builds</div></div>
<div class="fine" style="right:24px;bottom:20px;color:#fff;text-shadow:0 1px 3px #000">*Draft: price and inclusions for Nathan to confirm</div>
""",
"4-can-it-come-down": """
<div style="position:absolute;inset:0;background:#1B1C1F"></div>
<img src="src/kd-12.5.jpg" style="position:absolute;left:0;right:0;bottom:150px;width:100%;height:600px;object-fit:cover;object-position:50% 45%">
<div style="position:absolute;left:0;right:0;bottom:150px;height:600px;background:linear-gradient(180deg,#1B1C1F 0%,rgba(27,28,31,0) 30%)"></div>
<div style="position:absolute;left:64px;right:64px;top:84px;color:#fff">
 <div style="font-size:26px;letter-spacing:.14em;font-weight:700;color:#EB2227">BEFORE YOU SELL OR RENOVATE</div>
 <div style="font-size:84px;font-weight:800;line-height:1.05;margin-top:24px">Some Wynnum houses can't legally be knocked down.</div>
 <div style="font-size:58px;font-weight:600;margin-top:28px;color:#EB2227">Is yours one of them?</div>
</div>
<div class="bar" style="background:#fff"><img src="src/sabre-logo.png"><span class="btn">Check your street</span></div>
""",
"5-nathan-rating": """
<img class="bg" src="src/kd-1.jpg" style="object-position:50% 30%;height:960px">
<div style="position:absolute;left:0;right:0;top:0;height:1000px;background:linear-gradient(180deg,rgba(0,0,0,0) 60%,rgba(0,0,0,.45))"></div>
<div style="position:absolute;left:48px;top:48px;background:#fff;border-radius:14px;padding:14px 22px;box-shadow:0 6px 24px rgba(0,0,0,.25);display:flex;align-items:center;gap:14px">
 <span style="font-size:40px;font-weight:800">4.5</span><span class="stars">★★★★<span class="half">★</span></span><span style="font-size:24px;font-weight:600;color:#555">Google · 12 reviews</span></div>
<div style="position:absolute;left:0;right:0;top:900px;bottom:0;background:#fff;border-radius:34px 34px 0 0;padding:64px 56px">
 <div style="font-size:52px;font-weight:800;line-height:1.1">Nathan walks your old house.<br><span class="red">Then he answers the phone</span><br>the day you get the keys.</div>
 <div style="display:flex;justify-content:space-between;align-items:center;margin-top:36px">
  <div style="font-size:26px;color:#555;line-height:1.35"><b style="color:#1B1C1F">Nathan Brain</b> · Sabre Constructions<br>Building on the Bayside since 1990</div>
  <span class="btn" style="font-size:30px;padding:20px 28px">Book a walk-through</span></div>
</div>
""",
}

for name, body in ADS.items():
    h = M / f"{name}.html"
    h.write_text(HEAD + body + "</body></html>", encoding="utf-8")
    png = M / f"{name}.png"
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--window-size=1080,1350", "--virtual-time-budget=6000",
                    f"--screenshot={png}", h.as_uri()], check=True, capture_output=True)
    print("rendered", png.name, png.stat().st_size)
