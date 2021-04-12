package com.example.myapplication
import retrofit2.Call
import retrofit2.http.Field
import retrofit2.http.FormUrlEncoded
import retrofit2.http.POST

interface LoginService {
    @FormUrlEncoded //server에서 값을 못받아오는 것을 막음
    @POST("/app_login/")
    fun requestLogin(
        //input
        @Field("userid") userid:String,
        @Field("userpw") userpw:String
    ): Call<Login> //output
}