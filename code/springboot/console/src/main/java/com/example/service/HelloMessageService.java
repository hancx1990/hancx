package com.example.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
public class HelloMessageService {

	@Value("${name:unknown}")
	private String name;
	
	public String getMessage() {
		return getMessage(name);
	}

	public String getMessage(String name2) {
		return "Hello " + name;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	
	
}
