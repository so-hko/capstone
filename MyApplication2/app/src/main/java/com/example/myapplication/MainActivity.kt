package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.EditText
import androidx.appcompat.app.AlertDialog
import kotlinx.android.synthetic.main.activity_main.*;
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        //retrofit 객체
        var retrofit=Retrofit.Builder().baseUrl("http://192.168.0.6:8000")
            .addConverterFactory(GsonConverterFactory.create()).build()

        //service를 호출할 수 있는 service interface
        var loginServie=retrofit.create(LoginService::class.java)

        editTextTextPersonName
        button.setOnClickListener{
            var textId=editTextTextPersonName.text.toString()
            var textPassword=editTextTextPassword.text.toString()

            loginServie.requestLogin(textId,textPassword).enqueue(object: Callback<Login>{
                override fun onFailure(call: Call<Login>, t: Throwable) {
                    //웹통신에 실패했을 때 실행되는 코드
                    var dialog=AlertDialog.Builder(this@MainActivity)
                    dialog.setTitle("실패!")
                    dialog.setMessage("통신에 실패했습니다")
                    dialog.show()
                }

                override fun onResponse(call: Call<Login>, response: Response<Login>) {
                    //웹통신에 성공했을 때 응답값을 받아옴
                    var login=response.body() //code, msg
                    var dialog=AlertDialog.Builder(this@MainActivity)
                    dialog.setTitle("알람!")
                    dialog.setMessage("code = "+login?.code+" msg = "+login?.msg) //?는 null일 수 도 있을 때 사용
                    dialog.show()
                }

            })

        }
    }
}

