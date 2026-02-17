import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService, Apartment } from './api.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  template: `
    <h2>Apartments List</h2>

    <div *ngFor="let apt of apartments" 
         style="border:1px solid #ccc; padding:10px; margin:10px;">

      <h3>{{ apt.title }}</h3>
      <p>Price: ₹{{ apt.price }}</p>
      <p>Location: {{ apt.location }}</p>
      <p>Category: {{ apt.category_name }}</p>

    </div>
  `
})
export class App implements OnInit {

  apartments: Apartment[] = [];

  constructor(private api: ApiService) {}

  ngOnInit() {
    this.api.getApartments().subscribe(data => {
      this.apartments = data;
    });
  }
}

