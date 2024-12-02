package com.example.energyconsumption

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Update text dynamically (example)
        val lastHourValue = findViewById<TextView>(R.id.lastHourValue)
        val lastDayValue = findViewById<TextView>(R.id.lastDayValue)
        val lastMonthValue = findViewById<TextView>(R.id.lastMonthValue)

        // These values can be fetched from a database or API
        lastHourValue.text = "0.5 kWh"
        lastDayValue.text = "17 kWh"
        lastMonthValue.text = "42 kWh"
        // https://docs.google.com/document/d/1CHlFzsM-VV8RxX47YIVPvKISz0tgZjTv-O8PoUgAUI0/edit?usp=sharing
    }
}
