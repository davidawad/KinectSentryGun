package com.example.demo.kinectsentrygun;

import android.content.Intent;
import android.graphics.Color;
import android.net.Uri;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.content.Context;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.net.URI;


public class MainActivity extends ActionBarActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    Button fire;
    Button twitter;
    Button remove_twitter;
    TextView textybox;
    Context ctx;


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);

        setContentView(R.layout.activity_main);
        // ctx is set. ctx is a pointer to the current rendered context on the Android device.
        ctx = this;
        //  next button pointer
        twitter = (Button) findViewById(R.id.button1);
        fire = (Button) findViewById(R.id.button2);
        remove_twitter = (Button) findViewById(R.id.button3);
        // output where text will be displayed
        textybox = (TextView) findViewById(R.id.textView3);


        fire.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(Intent.ACTION_VIEW).setData(Uri.parse("https://www.youtube.com/watch?v=5VJsE5mrT44&feature=youtu.be")));
            }

        });




        twitter.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(Intent.ACTION_VIEW).setData(Uri.parse("https://twitter.com/kinectsentrygun")));
            }

        });

        remove_twitter.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
//                MediaPlayer mPlayer = MediaPlayer.create(getBaseContext(), R.raw.I_Got_Shot);
//                mPlayer.start();
                startActivity(new Intent(Intent.ACTION_VIEW).setData(Uri.parse("http://kinectsentrygun.projects.benhgreen.com/")));
            }

        });


    return true;
    }

}