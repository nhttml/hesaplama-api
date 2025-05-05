from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hesapla', methods=['POST'])
def home():
    return jsonify({"message": "API çalışıyor!"})
def hesapla():
    data = request.json

    try:
        alisfiyat = float(data['alisfiyat'])
        satisfiyat = float(data['satisfiyat'])
        kdvorani = int(data['kdvorani'])
        kargotutari = float(data['kargotutari'])
        komisyon = float(data['komisyon'])
        masraf = float(data['masraf'])

        kdvdhlfyt = alisfiyat + (alisfiyat * kdvorani) / 100
        alskdvttr = kdvdhlfyt - kdvdhlfyt / (1 + kdvorani / 100)
        krgkdvttr = kargotutari * 1.2 - kargotutari
        stskdv = satisfiyat - satisfiyat / (1 + kdvorani / 100)
        kmsynttr = (satisfiyat * komisyon) / 100
        kmsynkdvttr = kmsynttr - kmsynttr / (1 + 20 / 100)
        kdvfrk = stskdv - kmsynkdvttr - krgkdvttr - alskdvttr
        hkeds = satisfiyat - kargotutari - kmsynttr - krgkdvttr - 5.99
        tplmkar = hkeds - kdvfrk - alisfiyat - masraf

        return jsonify({
            "sonuc": round(tplmkar, 2),
            "aliskdv": round(alskdvttr, 2),
            "kargokdv": round(krgkdvttr, 2),
            "komkdv": round(kmsynkdvttr, 2),
            "satiskdv": round(stskdv, 2),
            "kdvfark": round(kdvfrk, 2),
            "hakedis": round(hkeds, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run()
