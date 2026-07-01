import { useEffect, useState } from "react";
import api from "./services/api";

function App() {
  const [companies, setCompanies] = useState([]);
  const [customers, setCustomers] = useState([]);
  const [selectedCompany, setSelectedCompany] = useState("");

  useEffect(() => {
    loadCompanies();
  }, []);

  const loadCompanies = async () => {
    try {
      const response = await api.get("/companies");
      setCompanies(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  const loadCustomers = async (companyId) => {
    try {
      const response = await api.get(`/customers/${companyId}`);
      setCustomers(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {

    if (!selectedCompany) return;

    const interval = setInterval(() => {
        loadCustomers(selectedCompany);
    }, 5000);

    return () => clearInterval(interval);

}, [selectedCompany]);

  const triggerCampaign = async () => {

    if (!selectedCompany) {

        alert("Please select a company");

        return;

    }

    try {

        const response = await api.post(`/campaign/${selectedCompany}`);

        alert(response.data.message);

        loadCustomers(selectedCompany);

    }

    catch (error) {

        console.log(error);

    }

};


const refreshCustomers = async () => {

    if (!selectedCompany) {

        alert("Please select a company");

        return;

    }

    await loadCustomers(selectedCompany);

    alert("Customer status refreshed!");
};

  const handleCompanyChange = (e) => {
    const companyId = e.target.value;
    setSelectedCompany(companyId);

    if (companyId) {
      loadCustomers(companyId);
    } else {
      setCustomers([]);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-950 to-black py-10">

      <div className="max-w-6xl mx-auto">

        <h1 className="text-5xl font-bold text-center text-white">
          🎙 Voice AI Dashboard
        </h1>

        <p className="text-center text-gray-300 mt-2 mb-8">
          AI Powered Multi-Tenant Calling Platform
         </p>

        <div className="bg-white rounded-xl shadow-2xl p-8">

          <div className="mb-6">

            <label className="block font-semibold mb-2">
              Select Company
            </label>

            <select
              value={selectedCompany}
              onChange={handleCompanyChange}
              className="w-full border rounded-lg p-3"
            >
              <option value="">Select Company</option>

              {companies.map((company) => (
                <option key={company._id} value={company._id}>
                  {company.name}
                </option>
              ))}
            </select>

          </div>


          <div className="grid grid-cols-4 gap-5 my-8">

                <div className="bg-blue-100 rounded-xl p-5">
                <h2 className="text-3xl font-bold">{customers.length}</h2>
                <p>Total Customers</p>
                </div>

                <div className="bg-green-100 rounded-xl p-5">
                <h2 className="text-3xl font-bold">
                {customers.filter(c=>c.status==="QUALIFIED").length}
                </h2>
                <p>Qualified</p>
                </div>

                <div className="bg-yellow-100 rounded-xl p-5">
                <h2 className="text-3xl font-bold">
                {customers.filter(c=>c.status==="NEEDS_REVIEW").length}
                </h2>
                <p>Need Review</p>
                </div>

                <div className="bg-purple-100 rounded-xl p-5">
                <h2 className="text-3xl font-bold">
                {customers.filter(c=>c.status==="CALL_INITIATED").length}
                </h2>
                <p>Calling</p>
                </div>

                </div>

          <table className="w-full border-collapse overflow-hidden rounded-xl shadow">

            <thead className="bg-slate-800 text-white">

              <tr className="hover:bg-slate-100 transition">

                <th className="border p-4">Name</th>

                <th className="border p-4">Phone</th>

                <th className="border p-4">Status</th>

              </tr>

            </thead>

            <tbody>

              {customers.map((customer) => (

                <tr key={customer._id}>

                  <td className="border p-3">{customer.name}</td>

                  <td className="border p-3">{customer.phone}</td>

                  <td className="border p-3">

                   
                         <span
                              className={`px-4 py-2 rounded-full text-white text-sm font-semibold

                              ${
                              customer.status==="QUALIFIED"
                              ?"bg-green-500"

                              :customer.status==="NEEDS_REVIEW"
                              ?"bg-yellow-500"

                              :customer.status==="CALL_INITIATED"
                              ?"bg-blue-500"

                              :"bg-red-500"

                              }`}
                              >

                              {customer.status}

                              </span>

                  </td>

                </tr>

              ))}

            </tbody>

          </table>

          <div className="flex gap-4 mt-6">

            <button

              onClick={triggerCampaign}

              className="mt-8 w-full bg-gradient-to-r from-blue-600 to-indigo-600 text-white py-4 rounded-xl font-bold text-lg hover:scale-105 transition"

              >

              Trigger Campaign

              </button>

            <button

             onClick={refreshCustomers}

              className="bg-gray-700 text-white px-6 py-2 rounded-lg hover:bg-gray-800"

            >        
                Refresh Status

            </button>

           </div>

        </div>

      </div>

    </div>
  );
}

export default App;