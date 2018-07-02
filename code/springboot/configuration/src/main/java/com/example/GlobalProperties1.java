package com.example;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.PropertySource;
import org.springframework.stereotype.Component;

@Component
@PropertySource("classpath:gobal.properties")
@ConfigurationProperties
public class GlobalProperties1 {

	private int threadPool;
	private String email;
	public int getThreadPool() {
		return threadPool;
	}
	public void setThreadPool(int threadPool) {
		this.threadPool = threadPool;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	
}
