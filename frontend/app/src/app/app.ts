import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class AppComponent implements OnInit {

  apartments: any[] = [];

  newApartment = {
    title: '',
    price: 0,
    location: '',
    category_id: 1
  };

  backendUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.loadApartments();
  }

  loadApartments() {
    this.http.get<any[]>(`${this.backendUrl}/apartments`)
      .subscribe(data => {
        this.apartments = data;
      });
  }

  addApartment() {
    this.http.post(`${this.backendUrl}/apartments`, this.newApartment)
      .subscribe(() => {
        this.loadApartments();
        this.newApartment = { title: '', price: 0, location: '', category_id: 1 };
      });
  }

  deleteApartment(id: number) {
    this.http.delete(`${this.backendUrl}/apartments/${id}`)
      .subscribe(() => {
        this.loadApartments();
      });
  }
}

