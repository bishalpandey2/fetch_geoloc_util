/// <reference types="cypress" />

describe("Geolocation API Tests", () => {
  const API_KEY = "f897a99d971b5eef57be6fafa0d83239";
  const BASE_URL = "http://api.openweathermap.org/geo/1.0";

  interface GeoResponse {
    name: string;
    lat: number;
    lon: number;
  }

  function checkGeoResponse(response: Cypress.Response<GeoResponse | GeoResponse[]>) {
    expect(response.status).to.eq(200);
    expect(response.body).to.not.be.null;
    expect(response.duration).to.be.lessThan(2000);
  }

  it("Should return correct geolocation for a city", () => {
    cy.request<GeoResponse[]>(`${BASE_URL}/direct?q=Madison,WI,US&limit=1&appid=${API_KEY}`)
      .then((response) => {
        checkGeoResponse(response);
        expect(response.body[0].name).to.eq("Madison");
      });
  });

  it("Should return correct geolocation for a zip code", () => {
    cy.request<GeoResponse>(`${BASE_URL}/zip?zip=10001,US&appid=${API_KEY}`)
      .then((response) => {
        checkGeoResponse(response);
        expect(response.body.name).to.eq("New York");
      });
  });

  it("Should handle multiple location inputs", () => {
    const locations = ["Madison,WI", "10001"];
    locations.forEach((location) => {
      const endpoint = /^\d+$/.test(location) ? "zip" : "direct";
      const query = endpoint === "zip" ? `zip=${location},US` : `q=${location},US&limit=1`;
      cy.request(`${BASE_URL}/${endpoint}?${query}&appid=${API_KEY}`)
        .then(checkGeoResponse);
    });
  });

  it("Should return an empty array for invalid city", () => {
    cy.request<GeoResponse[]>(`${BASE_URL}/direct?q=InvalidCity,US&limit=1&appid=${API_KEY}`)
      .then((response) => {
        expect(response.status).to.eq(200);
        expect(response.body).to.be.an("array").that.is.empty;
      });
  });

  it("Should return 404 for invalid zip code", () => {
    cy.request({
      url: `${BASE_URL}/zip?zip=99999,US&appid=${API_KEY}`,
      failOnStatusCode: false,
    }).then((response) => {
      expect(response.status).to.eq(404);
    });
  });
});
