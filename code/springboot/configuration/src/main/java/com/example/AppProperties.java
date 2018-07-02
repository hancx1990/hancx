package com.example;

import java.util.ArrayList;
import java.util.List;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

@Component
@ConfigurationProperties("app")
public class AppProperties {
	private String error;
	private List<Menu> menus = new ArrayList<>();
	private Compiler compiler = new Compiler();
	public String getError() {
		return error;
	}
	public void setError(String error) {
		this.error = error;
	}
	public List<Menu> getMenus() {
		return menus;
	}
	public void setMenus(List<Menu> menus) {
		this.menus = menus;
	}
	public Compiler getCompiler() {
		return compiler;
	}
	public void setCompiler(Compiler compiler) {
		this.compiler = compiler;
	}
	
}

